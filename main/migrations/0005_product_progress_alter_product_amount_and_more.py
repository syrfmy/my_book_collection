# Generated by Django 4.2.5 on 2023-09-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_author_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='progress',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
