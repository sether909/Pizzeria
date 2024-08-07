# Generated by Django 4.2.13 on 2024-07-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pizzas", "0003_pizza_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pizza",
            name="image",
            field=models.ImageField(
                blank=True, default="fallback_image.jpg", upload_to="pizza_images/"
            ),
        ),
    ]
