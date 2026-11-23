from django.shortcuts import redirect

from company_site.rendering import crumbs, respond
from company_site.views import render_not_found

from .content import BRANDS, PRODUCTS, cards, catalog_menu, category_with_count, find_category, find_product, products_in, related

SECTION_TITLE = "Catalog"
SECTION_URL = "/catalog/"


def category_links():
    return [{"slug": item["slug"], "title": item["short_title"], "icon": item["icon"], "url": item["url"]} for item in catalog_menu()]


def index(request):
    data = {
        "title": "DJ Equipment Catalog",
        "subtitle": "Every product is tested in our demo booth before it ships.",
        "categories": catalog_menu(),
        "products": cards(PRODUCTS),
        "brands": BRANDS,
    }
    return respond(
        request, "catalog", SECTION_TITLE, "catalog/catalog.html", data,
        subsections=category_links(), breadcrumbs=crumbs((SECTION_TITLE, SECTION_URL)),
    )


def category(request, category):
    current = find_category(category)
    if not current:
        return redirect(SECTION_URL)
    items = products_in(category)
    data = {
        "category": category_with_count(current),
        "products": cards(items),
        "brands": sorted({item["brand"] for item in items}),
    }
    return respond(
        request, "catalog", current["title"], "catalog/category.html", data,
        section_title=SECTION_TITLE, subsection=category, subsections=category_links(),
        breadcrumbs=crumbs((SECTION_TITLE, SECTION_URL), (current["short_title"], f"{SECTION_URL}{category}/")),
    )


def product(request, category, product):
    current = find_category(category)
    if not current:
        return redirect(SECTION_URL)
    item = find_product(category, product)
    if not item:
        return render_not_found(request)
    data = {"product": item, "category": category_with_count(current), "related": related(item)}
    return respond(
        request, "catalog", item["name"], "catalog/product.html", data,
        section_title=SECTION_TITLE, subsection=category, subsections=category_links(),
        breadcrumbs=crumbs((SECTION_TITLE, SECTION_URL), (current["short_title"], f"{SECTION_URL}{category}/"), (item["name"], item["url"])),
    )


def fallback(request):
    return redirect(SECTION_URL)
