# Generated by Django 4.2.3 on 2023-08-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(default=False, verbose_name='Auction'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]