from django.db import models
from django.utils import timezone

# NOT NULL 이 기본옵션

class User(models.Model):
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)


    def __str__(self):
        return self.email


class Item(models.Model):
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=50)
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    rate = models.CharField(max_length=20, default='0')
    like_user_set = models.ManyToManyField('User', null=True,
                                            blank=True, related_name='like_user_set',
                                             through='Like')
    img_url = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default='')
    
    class Meta:
        ordering = ['-rate']

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.like_user_set.count()

class Like(models.Model):
    user = models.ForeignKey('User')
    item = models.ForeignKey('Item')
    created_date = models.DateTimeField(default=timezone.now)


class Brand(models.Model):
    company = models.CharField(max_length=50)
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.company