
from taggit.managers import TaggableManager
from django.db import models

# Create your models here.



class News(models.Model):
    TitleNews = models.CharField('Название', max_length=50)
    SomeNews = models.TextField('Новость')
    Author = models.CharField('Автор', max_length=50)
    TimeCreate = models.DateTimeField('Время создания', auto_now_add=True)
    Image = models.ImageField(upload_to='images/', default='images/notfing.jpg')
    Tags = TaggableManager('Теги')

    def __str__(self):
        return self.TitleNews

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
