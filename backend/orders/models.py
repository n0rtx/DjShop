from django.conf import settings
from django.db import models


class Order(models.Model):
    class Delivery(models.TextChoices):
        COURIER = "courier", "Courier to the door"
        POST = "post", "Nova Poshta branch"
        PICKUP = "pickup", "Pickup at the Odesa showroom"

    class Payment(models.TextChoices):
        CARD = "card", "Card on delivery"
        CASH = "cash", "Cash on delivery"
        INVOICE = "invoice", "Bank invoice"

    class Status(models.TextChoices):
        COMPLETED = "completed", "Completed"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    full_name = models.CharField("Full name", max_length=120)
    phone = models.CharField("Phone", max_length=20)
    email = models.EmailField("Email")
    city = models.CharField("City", max_length=80)
    address = models.CharField("Address", max_length=200, blank=True)
    delivery = models.CharField("Delivery", max_length=20, choices=Delivery.choices, default=Delivery.COURIER)
    payment = models.CharField("Payment", max_length=20, choices=Payment.choices, default=Payment.CARD)
    comment = models.TextField("Comment", blank=True)
    status = models.CharField("Status", max_length=20, choices=Status.choices, default=Status.COMPLETED)
    total = models.DecimalField("Total, USD", max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField("Created", auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return f"{self.number} — {self.full_name}"

    @property
    def number(self):
        return f"NP-{self.pk:05d}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_id = models.PositiveIntegerField("Product ID")
    sku = models.CharField("SKU", max_length=30)
    name = models.CharField("Name", max_length=160)
    brand = models.CharField("Brand", max_length=60)
    image = models.CharField("Image", max_length=255)
    url = models.CharField("URL", max_length=255)
    price = models.DecimalField("Price, USD", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Quantity", default=1)

    def __str__(self):
        return f"{self.name} × {self.quantity}"

    @property
    def line_total(self):
        return self.price * self.quantity
