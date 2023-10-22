# Generated by Django 4.2.5 on 2023-10-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_item_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='available_count',
            field=models.PositiveIntegerField(default=0, help_text='Number of items available'),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_count',
            field=models.PositiveIntegerField(default=0, help_text='Number of purchases'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]