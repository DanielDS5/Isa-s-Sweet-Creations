# Generated by Django 4.1.5 on 2023-01-25 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_alter_cakes_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cakes",
            old_name="imagen",
            new_name="image",
        ),
    ]