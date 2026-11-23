from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("number", "user", "full_name", "city", "delivery", "total", "status", "created_at")
    list_filter = ("status", "delivery", "payment", "created_at")
    search_fields = ("full_name", "email", "phone", "user__username")
    inlines = [OrderItemInline]
