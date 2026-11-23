import json

from django import forms
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme

from .rendering import allow_frontend_origin, wants_json


def form_data(request):
    if request.method != "POST":
        return None
    if request.content_type == "application/json":
        try:
            data = json.loads(request.body or b"{}")
        except ValueError:
            return {}
        return data if isinstance(data, dict) else {}
    return request.POST


def safe_next(request, default):
    target = request.GET.get("next") or ""
    if target and url_has_allowed_host_and_scheme(target, allowed_hosts={request.get_host()}):
        return target
    return default


def field_type(bound):
    widget = bound.field.widget
    if isinstance(widget, forms.Textarea):
        return "textarea"
    if isinstance(widget, forms.RadioSelect):
        return "radio"
    if isinstance(widget, forms.Select):
        return "select"
    return getattr(widget, "input_type", "text")


def field_value(bound, kind):
    if kind == "password":
        return ""
    value = bound.value()
    return "" if value is None else str(value)


def form_schema(form):
    fields = []
    for bound in form.visible_fields():
        kind = field_type(bound)
        item = {
            "name": bound.name,
            "label": str(bound.label),
            "type": kind,
            "required": bound.field.required,
            "value": field_value(bound, kind),
            "help": str(bound.help_text or ""),
            "placeholder": bound.field.widget.attrs.get("placeholder", ""),
            "autocomplete": bound.field.widget.attrs.get("autocomplete", ""),
            "errors": [str(error) for error in bound.errors],
        }
        if kind in ("select", "radio"):
            item["choices"] = [{"value": str(value), "label": str(label)} for value, label in bound.field.choices]
        fields.append(item)
    errors = [str(error) for error in form.non_field_errors()]
    errors += [str(error) for bound in form.hidden_fields() for error in bound.errors]
    return {"fields": fields, "errors": errors}


def handle_form(request, form, on_valid, render_page):
    if request.method == "POST":
        if form.is_valid():
            target = on_valid(form)
            if wants_json(request):
                return allow_frontend_origin(request, JsonResponse({"ok": True, "redirect": target}))
            return redirect(target)
        if wants_json(request):
            return allow_frontend_origin(request, JsonResponse({"ok": False, "form": form_schema(form)}, status=400))
    return render_page(form)
