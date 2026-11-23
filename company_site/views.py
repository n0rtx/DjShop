from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .content import PAGES, SITE


def wants_json(request):
    if request.GET.get("format") == "json":
        return True
    accept = request.headers.get("Accept", "")
    return "application/json" in accept and "text/html" not in accept


def build_payload(request, page_key):
    page = PAGES[page_key]
    return {
        "page": page_key,
        "title": page["title"],
        "path": request.path,
        "site": SITE,
        "data": page["data"],
    }


def allow_frontend_origin(request, response):
    origin = request.headers.get("Origin")
    if origin and origin in settings.FRONTEND_ORIGINS:
        response["Access-Control-Allow-Origin"] = origin
        response["Vary"] = "Origin"
    return response


def render_page(request, page_key):
    payload = build_payload(request, page_key)
    if wants_json(request):
        response = JsonResponse(payload, json_dumps_params={"ensure_ascii": False})
    else:
        response = render(request, f"{page_key}.html", {"payload": payload, **payload})
    return allow_frontend_origin(request, response)


def home(request):
    return render_page(request, "home")


def news(request, _=None):
    return render_page(request, "news")


def management(request, _=None):
    return render_page(request, "management")


def about(request, _=None):
    return render_page(request, "about")


def contacts(request, _=None):
    return render_page(request, "contacts")
