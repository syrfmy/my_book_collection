# Generated by Django 4.2.5 on 2023-09-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_price_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='no_author', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='no_name', max_length=255),
        ),
    ]