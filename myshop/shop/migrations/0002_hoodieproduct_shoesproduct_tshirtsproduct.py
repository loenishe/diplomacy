# Generated by Django 3.1.7 on 2021-03-13 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TShirtsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер Футболок')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя Футболок')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Футболки для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShoesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер кроссовок')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя кроссовок')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Кроссовок для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HoodieProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер Худи')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Брендовое имя Худи')),
                ('sex', models.CharField(max_length=255, verbose_name='Пол')),
                ('season', models.CharField(max_length=255, verbose_name='Худи для Сезона')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
