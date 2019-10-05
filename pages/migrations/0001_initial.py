# Generated by Django 2.2.6 on 2019-10-05 12:49

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Название фильтра')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Фильтр',
                'verbose_name_plural': 'Фильтры',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, upload_to='portfolio_img/', verbose_name='Изображение')),
                ('client', models.CharField(default='', max_length=255, verbose_name='Клиент')),
                ('date', models.CharField(default='', max_length=100, verbose_name='Дата')),
                ('url', models.CharField(default='', max_length=100, verbose_name='Ссылка')),
                ('wishes', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Пожелания')),
                ('technical', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Решения')),
                ('progressBarBackEnd', models.IntegerField(default=0, verbose_name='Прогресс-бар BackEnd')),
                ('progressBarFrontEnd', models.IntegerField(default=0, verbose_name='Прогресс-бар FrontEnd')),
                ('progressBarProduction', models.IntegerField(default=0, verbose_name='Прогресс-бар Production')),
                ('progressBarSEO', models.IntegerField(default=0, verbose_name='Прогресс-бар SEO')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Отображать ?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Filter', verbose_name='Фильтр')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Статус')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(default='#', max_length=100, verbose_name='Цвет в виде #000000')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_img/', verbose_name='Картинка')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.PortfolioItem', verbose_name='Кейс')),
            ],
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.Status', verbose_name='Текущий статус'),
        ),
    ]