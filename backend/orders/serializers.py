def order_to_dict(order):
    items = list(order.items.all())
    return {
        "id": order.pk,
        "number": order.number,
        "created": order.created_at.isoformat(),
        "status": order.get_status_display(),
        "status_key": order.status,
        "full_name": order.full_name,
        "phone": order.phone,
        "email": order.email,
        "city": order.city,
        "address": order.address,
        "delivery": order.get_delivery_display(),
        "payment": order.get_payment_display(),
        "comment": order.comment,
        "total": float(order.total),
        "count": sum(item.quantity for item in items),
        "items": [
            {
                "product_id": item.product_id,
                "sku": item.sku,
                "name": item.name,
                "brand": item.brand,
                "image": item.image,
                "url": item.url,
                "price": float(item.price),
                "qty": item.quantity,
                "line_total": float(item.line_total),
            }
            for item in items
        ],
    }
