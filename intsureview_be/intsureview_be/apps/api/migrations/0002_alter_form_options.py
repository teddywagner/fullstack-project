# Generated by Django 4.2.3 on 2023-07-17 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="form", options={"ordering": ["id"]},),
    ]