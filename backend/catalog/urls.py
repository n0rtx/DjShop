from django.urls import path, re_path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^(?P<category>[\w-]+)/?$", views.category, name="category"),
    re_path(r"^(?P<category>[\w-]+)/(?P<product>[\w-]+)/?$", views.product, name="product"),
    re_path(r"^.+$", views.fallback, name="fallback"),
]
