# Generated by Django 4.2.10 on 2024-03-09 17:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='name', unique_with=['id', 'created_at']),
        ),
    ]