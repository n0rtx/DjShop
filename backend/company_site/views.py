from django.shortcuts import redirect
from django.urls import Resolver404, resolve

from .content import PAGES, SUBSECTIONS, find_article, find_subsection
from .rendering import crumbs, respond


def subsection_links(page_key):
    return [
        {"slug": item["slug"], "title": item["title"], "icon": item["icon"], "url": f"/{page_key}/{item['slug']}/"}
        for item in SUBSECTIONS.get(page_key, [])
    ]


def render_section(request, page_key, subsection_slug=None):
    page = PAGES[page_key]
    section_url = f"/{page_key}/"
    subsection = find_subsection(page_key, subsection_slug)
    if subsection_slug and not subsection:
        return redirect(section_url)
    if subsection:
        return respond(
            request, page_key, subsection["title"], f"{page_key}_detail.html", subsection["data"],
            section_title=page["title"], subsection=subsection["slug"], subsections=subsection_links(page_key),
            breadcrumbs=crumbs((page["title"], section_url), (subsection["title"], request.path)),
        )
    return respond(
        request, page_key, page["title"], f"{page_key}.html", page["data"],
        subsections=subsection_links(page_key), breadcrumbs=crumbs((page["title"], section_url)),
    )


def home(request):
    return respond(request, "home", "Home", "home.html", PAGES["home"]["data"])


def news(request, subsection=None):
    return render_section(request, "news", subsection)


def management(request, subsection=None):
    return render_section(request, "management", subsection)


def about(request, subsection=None):
    return render_section(request, "about", subsection)


def contacts(request, subsection=None):
    return render_section(request, "contacts", subsection)


def news_article(request, subsection, article):
    item = find_article(subsection, article)
    if not item:
        return redirect(f"/news/{subsection}/")
    tag = find_subsection("news", subsection)
    return respond(
        request, "news", item["title"], "news_article.html", item,
        section_title="News", subsection=subsection, subsections=subsection_links("news"),
        breadcrumbs=crumbs(("News", "/news/"), (tag["title"], f"/news/{subsection}/"), (item["title"], request.path)),
    )


def section_fallback(request, section, rest=None):
    return redirect(f"/{section}/")


def legacy_contact(request, rest=""):
    return redirect(f"/contacts/{rest}", permanent=True)


def render_not_found(request):
    return respond(request, "not_found", "Page not found", "404.html", PAGES["not_found"]["data"], status=404)


def not_found(request, exception=None):
    if not request.path.endswith("/"):
        try:
            match = resolve(f"{request.path}/")
            if match.url_name != "not-found":
                query = request.META.get("QUERY_STRING")
                return redirect(f"{request.path}/" + (f"?{query}" if query else ""))
        except Resolver404:
            pass
    return render_not_found(request)
