from urllib.parse import urlencode

from django.shortcuts import redirect

from company_site.forms_api import form_data, form_schema, handle_form
from company_site.rendering import crumbs, respond

from .forms import CheckoutForm
from .models import Order


def checkout_initial(user):
    initial = {"full_name": user.get_full_name() or user.first_name, "email": user.email}
    last = Order.objects.filter(user=user).first()
    if last:
        initial.update(phone=last.phone, city=last.city, address=last.address, delivery=last.delivery, payment=last.payment, full_name=last.full_name)
    return initial


def checkout(request):
    if not request.user.is_authenticated:
        return redirect(f"/account/login/?{urlencode({'next': '/checkout/'})}")
    form = CheckoutForm(form_data(request), initial=checkout_initial(request.user))

    def place(valid):
        order = valid.save_for(request.user)
        return f"/account/?order={order.pk}"

    def page(current):
        data = {
            "title": "Checkout",
            "subtitle": "This is a study project: the order goes straight to your order history, nothing is charged or shipped.",
            "form": form_schema(current),
        }
        return respond(request, "checkout", "Checkout", "orders/checkout.html", data, breadcrumbs=crumbs(("Checkout", "/checkout/")))

    return handle_form(request, form, place, page)
