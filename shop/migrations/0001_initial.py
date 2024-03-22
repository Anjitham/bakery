# Generated by Django 5.0.2 on 2024-03-22 10:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour_name', models.CharField(max_length=150, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occasion_name', models.CharField(max_length=150, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CakeVarient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='cake_images')),
                ('shape', models.CharField(choices=[('Round', 'Round'), ('Square', 'Square'), ('Rectangle', 'Rectangle'), ('Heart', 'Heart'), ('Custom', 'Custom')], default='custom', max_length=150)),
                ('weight', models.CharField(choices=[('250gm', '250gm'), ('500gm', '500gm'), ('1kg', '1kg'), ('2kg', '2kg'), ('Custom', 'Custom')], default='500', max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('cake_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakeitem', to='shop.cake')),
                ('cakecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('flavour_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.flavour')),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='occasion_object',
            field=models.ManyToManyField(to='shop.occasion'),
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=1)),
                ('is_order_placed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('basket_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='shop.basket')),
                ('cake_varient_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cakevarient', to='shop.cakevarient')),
                ('occasion_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.occasion')),
            ],
        ),
    ]
