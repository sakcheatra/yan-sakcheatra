# Generated by Django 5.2.4 on 2025-07-24 11:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('daily', 'Daily Report'), ('weekly', 'Weekly Report'), ('monthly', 'Monthly Report'), ('yearly', 'Yearly Report'), ('custom', 'Custom Date Range')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_orders', models.PositiveIntegerField(default=0)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total_items_sold', models.PositiveIntegerField(default=0)),
                ('average_order_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('is_cached', models.BooleanField(default=True)),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-generated_at'],
                'unique_together': {('report_type', 'start_date', 'end_date')},
            },
        ),
        migrations.CreateModel(
            name='ProductSalesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.PositiveIntegerField(default=0)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('average_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sales_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sales', to='reports.salesreport')),
            ],
            options={
                'unique_together': {('sales_report', 'product')},
            },
        ),
        migrations.CreateModel(
            name='CustomerSalesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_orders', models.PositiveIntegerField(default=0)),
                ('total_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('average_order_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sales_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_sales', to='reports.salesreport')),
            ],
            options={
                'unique_together': {('sales_report', 'customer')},
            },
        ),
    ]
