import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Full name')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.CharField(max_length=80, verbose_name='City')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Address')),
                ('delivery', models.CharField(choices=[('courier', 'Courier to the door'), ('post', 'Nova Poshta branch'), ('pickup', 'Pickup at the Odesa showroom')], default='courier', max_length=20, verbose_name='Delivery')),
                ('payment', models.CharField(choices=[('card', 'Card on delivery'), ('cash', 'Cash on delivery'), ('invoice', 'Bank invoice')], default='card', max_length=20, verbose_name='Payment')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('status', models.CharField(choices=[('completed', 'Completed')], default='completed', max_length=20, verbose_name='Status')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total, USD')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField(verbose_name='Product ID')),
                ('sku', models.CharField(max_length=30, verbose_name='SKU')),
                ('name', models.CharField(max_length=160, verbose_name='Name')),
                ('brand', models.CharField(max_length=60, verbose_name='Brand')),
                ('image', models.CharField(max_length=255, verbose_name='Image')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price, USD')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
        ),
    ]
