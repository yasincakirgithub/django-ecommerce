# Generated by Django 4.2.10 on 2024-03-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to='blog'),
            preserve_default=False,
        ),
    ]
