from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Filter(models.Model):
    name = models.CharField('Название фильтра', max_length=100, default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Filter, self).save(*args, **kwargs)

    def __str__(self):
        return 'Фильтр %s ' % self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


class Status(models.Model):
    name = models.CharField('Статус', max_length=100, default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField('Цвет в виде #000000', max_length=100, default='#')
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Status, self).save(*args, **kwargs)

    def __str__(self):
        return 'Статус %s ' % self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class PortfolioItem(models.Model):
    status = models.ForeignKey(Status,blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Текущий статус')
    filter = models.ForeignKey(Filter, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Фильтр')
    name = models.CharField('Название', max_length=255, default='')
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='portfolio_img/', blank=True)
    client = models.CharField('Клиент', max_length=255, default='')
    date = models.CharField('Дата', max_length=100, default='')
    url = models.CharField('Ссылка', max_length=100, default='')
    description = RichTextUploadingField('Описание', blank=True, null=True)
    wishes = RichTextUploadingField('Пожелания', blank=True, null=True)
    technical = RichTextUploadingField('Решения', blank=True, null=True)
    progressBarBackEnd = models.IntegerField('Прогресс-бар BackEnd', default=0)
    progressBarFrontEnd = models.IntegerField('Прогресс-бар FrontEnd', default=0)
    progressBarProduction = models.IntegerField('Прогресс-бар Production', default=0)
    progressBarSEO = models.IntegerField('Прогресс-бар SEO', default=0)
    is_active = models.BooleanField('Отображать на главной?', default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(PortfolioItem, self).save(*args, **kwargs)


    def __str__(self):
        return 'Кейс %s ' % self.name


    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"


class PortfolioItemImage(models.Model):
    item = models.ForeignKey(PortfolioItem, blank=False, null=True, on_delete=models.CASCADE, verbose_name='Кейс', related_name='porfolioItemImages')
    image = models.ImageField('Картинка', upload_to='portfolio_img/', blank=False)


class Callback(models.Model):
    name = models.CharField('Поле - Ваше имя',max_length=255, blank=False, default='Нет данных')
    company = models.CharField('Поле - Телефон', max_length=255, blank=True, default='Нет данных')
    phone = models.CharField('Поле - Телефон', max_length=255, blank=False, default='Нет данных')
    email = models.EmailField('Поле - Email', max_length=255, blank=True, default='Нет данных')
    message = models.TextField('Поле - Сообщение', max_length=255, blank=True, default='Нет данных')
