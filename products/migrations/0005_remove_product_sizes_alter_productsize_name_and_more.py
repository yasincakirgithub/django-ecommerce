# Generated by Django 4.2.10 on 2024-03-09 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_descrition_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AlterField(
            model_name='productsize',
            name='name',
            field=models.CharField(choices=[('xxl', 'xxl'), ('xl', 'xl'), ('l', 'l'), ('m', 'm'), ('s', 's'), ('xs', 'xs')], max_length=50),
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productsize')),
            ],
        ),
    ]