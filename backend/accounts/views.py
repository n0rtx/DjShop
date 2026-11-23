from urllib.parse import urlencode

from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.shortcuts import redirect

from company_site.forms_api import form_data, form_schema, handle_form, safe_next
from company_site.rendering import allow_frontend_origin, crumbs, respond, wants_json
from orders.serializers import order_to_dict

from .forms import LoginForm, RegisterForm

ACCOUNT_URL = "/account/"


def auth_page(request, page, title, template, form, subtitle, switch):
    data = {"title": title, "subtitle": subtitle, "form": form_schema(form), "switch": switch}
    return respond(request, page, title, template, data, breadcrumbs=crumbs(("Account", ACCOUNT_URL), (title, request.path)))


def with_next(url, next_url):
    return f"{url}?{urlencode({'next': next_url})}" if next_url != ACCOUNT_URL else url


def login_view(request):
    next_url = safe_next(request, ACCOUNT_URL)
    if request.user.is_authenticated and request.method == "GET":
        return redirect(next_url)
    form = LoginForm(request, data=form_data(request))

    def done(valid):
        login(request, valid.get_user())
        return next_url

    switch = {"text": "New to NEON PULSE?", "label": "Create an account", "url": with_next("/account/register/", next_url)}
    return handle_form(request, form, done, lambda current: auth_page(
        request, "login", "Sign in", "accounts/login.html", current, "Welcome back! Sign in to place orders and see your history.", switch,
    ))


def register_view(request):
    next_url = safe_next(request, ACCOUNT_URL)
    if request.user.is_authenticated and request.method == "GET":
        return redirect(next_url)
    form = RegisterForm(form_data(request))

    def done(valid):
        user = valid.save()
        login(request, user)
        return next_url

    switch = {"text": "Already have an account?", "label": "Sign in", "url": with_next("/account/login/", next_url)}
    return handle_form(request, form, done, lambda current: auth_page(
        request, "register", "Create account", "accounts/register.html", current, "Register to check out and keep every order in one place.", switch,
    ))


def logout_view(request):
    if request.method == "POST":
        logout(request)
        if wants_json(request):
            return allow_frontend_origin(request, JsonResponse({"ok": True, "redirect": "/"}))
        return redirect("/")
    return redirect(ACCOUNT_URL)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect(f"/account/login/?{urlencode({'next': ACCOUNT_URL})}")
    user = request.user
    orders = [order_to_dict(order) for order in user.orders.prefetch_related("items")]
    highlight = request.GET.get("order", "")
    data = {
        "profile": {
            "username": user.username,
            "name": user.first_name or user.username,
            "email": user.email,
            "joined": user.date_joined.isoformat(),
        },
        "stats": {
            "orders": len(orders),
            "items": sum(order["count"] for order in orders),
            "spent": round(sum(order["total"] for order in orders), 2),
        },
        "orders": orders,
        "highlight": int(highlight) if highlight.isdigit() else None,
    }
    return respond(request, "account", "My account", "accounts/account.html", data, breadcrumbs=crumbs(("Account", ACCOUNT_URL)))
