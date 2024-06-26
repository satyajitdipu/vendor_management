# Generated by Django 5.0.4 on 2024-05-02 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("contact_details", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("vendor_code", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("po_number", models.CharField(max_length=255)),
                ("vendor_reference", models.CharField(max_length=255)),
                ("order_date", models.DateField()),
                ("items", models.TextField()),
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=255)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vendor_app.vendor",
                    ),
                ),
            ],
        ),
    ]
