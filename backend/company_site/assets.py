from django.templatetags.static import static

ICON_BASE = "https://api.iconify.design/mdi"


def icon(name, color="6c3cff"):
    return f"{ICON_BASE}/{name}.svg?color=%23{color}"


def flag(code):
    return f"https://api.iconify.design/flag/{code}-4x3.svg"


def image(folder, slug):
    return static(f"img/{folder}/{slug}.jpg")
