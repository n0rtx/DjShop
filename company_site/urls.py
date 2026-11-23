from django.urls import path, re_path

from . import views
from .content import subsection_slugs


def subsection_route(prefix, section, view, name):
    slugs = "|".join(subsection_slugs(section))
    return re_path(rf"^{prefix}/(?P<subsection>{slugs})/?$", view, name=name)


urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news, name="news"),
    path("management/", views.management, name="management"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("contact/", views.contacts, name="contact-alt"),

    subsection_route("news", "news", views.news, "news-subsection"),
    subsection_route("management", "management", views.management, "mgmt-subsection"),
    subsection_route("about", "about", views.about, "about-subsection"),
    subsection_route("contacts", "contacts", views.contacts, "contacts-subsection"),
    subsection_route("contact", "contacts", views.contacts, "contact-alt-subsection"),

    path("news/<path:_>", views.news, name="news-catchall"),
    path("management/<path:_>", views.management, name="mgmt-catchall"),
    path("about/<path:_>", views.about, name="about-catchall"),
    path("contacts/<path:_>", views.contacts, name="contacts-catchall"),
    path("contact/<path:_>", views.contacts, name="contact-alt-catchall"),
]
