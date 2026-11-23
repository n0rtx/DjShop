from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views
from .content import subsection_slugs


def subsection_route(section, view):
    slugs = "|".join(subsection_slugs(section))
    return re_path(rf"^{section}/(?P<subsection>{slugs})/?$", view, name=f"{section}-subsection")


SECTIONS = "news|management|about|contacts"

urlpatterns = [
    path("", views.home, name="home"),
    path("catalog/", include("catalog.urls")),
    path("news/", views.news, name="news"),
    path("management/", views.management, name="management"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),

    subsection_route("news", views.news),
    subsection_route("management", views.management),
    subsection_route("about", views.about),
    subsection_route("contacts", views.contacts),

    re_path(rf"^news/(?P<subsection>{'|'.join(subsection_slugs('news'))})/(?P<article>[\w-]+)/?$", views.news_article, name="news-article"),

    re_path(r"^contact(?:/(?P<rest>.*))?$", views.legacy_contact, name="contact-legacy"),
    path("team/", RedirectView.as_view(url="/management/", permanent=True), name="team-legacy"),
    path("shop/", RedirectView.as_view(url="/catalog/", permanent=True), name="shop-legacy"),

    re_path(rf"^(?P<section>{SECTIONS})/(?P<rest>.+)$", views.section_fallback, name="section-fallback"),
    re_path(r"^.*$", views.not_found, name="not-found"),
]

handler404 = "company_site.views.not_found"
