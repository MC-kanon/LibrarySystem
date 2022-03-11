from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name='书籍名称', max_length=32)
    price = models.IntegerField(verbose_name='价格', default=0)
    info = models.CharField(max_length=64, verbose_name='书籍详情')
    authors = models.ManyToManyField(to="Author")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name='作者名')
    age = models.SmallIntegerField(verbose_name='年龄')
    phone = models.CharField(verbose_name='手机',max_length=32)

    def __str__(self):
        return self.name
