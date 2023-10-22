# Generated by Django 4.2.5 on 2023-10-19 19:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_alter_item_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Review text')),
                ('rating', models.PositiveIntegerField(help_text='The rating the reviewer has given', validators=[django.core.validators.MaxValueValidator(5, 'Rating cannot be greater than 5'), django.core.validators.MinValueValidator(1, 'Rating cannot be less than 1')])),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date and time of review')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(help_text='The item being sold', on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
        ),
    ]