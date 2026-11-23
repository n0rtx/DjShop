from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .content import SITE


def wants_json(request):
    if request.GET.get("format") == "json":
        return True
    accept = request.headers.get("Accept", "")
    return "application/json" in accept and "text/html" not in accept


def allow_frontend_origin(request, response):
    origin = request.headers.get("Origin")
    if origin and origin in settings.FRONTEND_ORIGINS:
        response["Access-Control-Allow-Origin"] = origin
        response["Vary"] = "Origin"
    return response


def crumbs(*items):
    return [{"title": "Home", "url": "/"}] + [{"title": title, "url": url} for title, url in items]


def respond(request, page, title, template, data, section_title=None, subsection=None, subsections=None, breadcrumbs=None, status=200):
    payload = {
        "page": page,
        "title": title,
        "section_title": section_title or title,
        "subsection": subsection,
        "subsections": subsections or [],
        "breadcrumbs": breadcrumbs or [],
        "path": request.path,
        "status": status,
        "site": SITE,
        "data": data,
    }
    if wants_json(request):
        response = JsonResponse(payload, status=status, json_dumps_params={"ensure_ascii": False})
    else:
        response = render(request, template, {"payload": payload, **payload}, status=status)
    return allow_frontend_origin(request, response)
