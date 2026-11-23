import re
from decimal import Decimal

from django import forms
from django.db import transaction

from catalog.content import PRODUCTS

from .models import Order, OrderItem

PRODUCTS_BY_ID = {item["id"]: item for item in PRODUCTS}
MAX_QTY = 20


class CheckoutForm(forms.ModelForm):
    items = forms.JSONField(widget=forms.HiddenInput, error_messages={"required": "Your cart is empty."})

    class Meta:
        model = Order
        fields = ("full_name", "phone", "email", "city", "delivery", "address", "payment", "comment")
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Taras Shevchenko", "autocomplete": "name"}),
            "phone": forms.TextInput(attrs={"placeholder": "+380 67 123 45 67", "autocomplete": "tel"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "autocomplete": "email"}),
            "city": forms.TextInput(attrs={"placeholder": "Odesa", "autocomplete": "address-level2"}),
            "address": forms.TextInput(attrs={"placeholder": "Street, building, apartment or branch number", "autocomplete": "street-address"}),
            "delivery": forms.RadioSelect,
            "payment": forms.RadioSelect,
            "comment": forms.Textarea(attrs={"rows": 3, "placeholder": "Anything we should know?"}),
        }
        help_texts = {"address": "Not needed for showroom pickup."}

    def clean_phone(self):
        phone = re.sub(r"[\s()-]", "", self.cleaned_data["phone"])
        if not re.fullmatch(r"\+?\d{10,15}", phone):
            raise forms.ValidationError("Enter a phone number with 10–15 digits.")
        return phone

    def clean_items(self):
        raw = self.cleaned_data.get("items")
        if not isinstance(raw, list) or not raw:
            raise forms.ValidationError("Your cart is empty.")
        lines = {}
        for entry in raw:
            try:
                pid, qty = int(entry["id"]), int(entry["qty"])
            except (KeyError, TypeError, ValueError):
                raise forms.ValidationError("Cart data is broken. Please clear the cart and try again.")
            product = PRODUCTS_BY_ID.get(pid)
            if not product:
                raise forms.ValidationError("Some products in your cart are no longer available.")
            if not product["in_stock"]:
                raise forms.ValidationError(f"{product['name']} is out of stock.")
            lines[pid] = lines.get(pid, 0) + qty
        for pid, qty in lines.items():
            if not 1 <= qty <= MAX_QTY:
                raise forms.ValidationError(f"Quantity of {PRODUCTS_BY_ID[pid]['name']} must be between 1 and {MAX_QTY}.")
        return [(PRODUCTS_BY_ID[pid], qty) for pid, qty in lines.items()]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("delivery") != Order.Delivery.PICKUP and not cleaned.get("address", "").strip():
            self.add_error("address", "Enter a delivery address or choose showroom pickup.")
        return cleaned

    def save_for(self, user):
        lines = self.cleaned_data["items"]
        with transaction.atomic():
            order = self.save(commit=False)
            order.user = user
            order.total = sum(Decimal(str(product["price"])) * qty for product, qty in lines)
            order.save()
            OrderItem.objects.bulk_create([
                OrderItem(
                    order=order,
                    product_id=product["id"],
                    sku=product["sku"],
                    name=product["name"],
                    brand=product["brand"],
                    image=product["image"],
                    url=product["url"],
                    price=Decimal(str(product["price"])),
                    quantity=qty,
                )
                for product, qty in lines
            ])
        return order
