from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .content import PAGES, SITE, SUBSECTIONS, find_subsection


def wants_json(request):
    if request.GET.get("format") == "json":
        return True
    accept = request.headers.get("Accept", "")
    return "application/json" in accept and "text/html" not in accept


def subsection_links(page_key):
    return [
        {"slug": item["slug"], "title": item["title"], "icon": item["icon"], "url": f"/{page_key}/{item['slug']}/"}
        for item in SUBSECTIONS.get(page_key, [])
    ]


def build_payload(request, page_key, subsection):
    page = PAGES[page_key]
    return {
        "page": page_key,
        "title": subsection["title"] if subsection else page["title"],
        "section_title": page["title"],
        "subsection": subsection["slug"] if subsection else None,
        "subsections": subsection_links(page_key),
        "path": request.path,
        "site": SITE,
        "data": subsection["data"] if subsection else page["data"],
    }


def allow_frontend_origin(request, response):
    origin = request.headers.get("Origin")
    if origin and origin in settings.FRONTEND_ORIGINS:
        response["Access-Control-Allow-Origin"] = origin
        response["Vary"] = "Origin"
    return response


def render_page(request, page_key, subsection_slug=None):
    subsection = find_subsection(page_key, subsection_slug)
    payload = build_payload(request, page_key, subsection)
    if wants_json(request):
        response = JsonResponse(payload, json_dumps_params={"ensure_ascii": False})
    else:
        template = f"{page_key}_detail.html" if subsection else f"{page_key}.html"
        response = render(request, template, {"payload": payload, **payload})
    return allow_frontend_origin(request, response)


def home(request):
    return render_page(request, "home")


def news(request, subsection=None, _=None):
    return render_page(request, "news", subsection)


def management(request, subsection=None, _=None):
    return render_page(request, "management", subsection)


def about(request, subsection=None, _=None):
    return render_page(request, "about", subsection)


def contacts(request, subsection=None, _=None):
    return render_page(request, "contacts", subsection)
