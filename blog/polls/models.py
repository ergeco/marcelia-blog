from django.db import models
from datetime import *
from django.utils import timezone


class Post(models.Model):
    title = models.TextField(max_length=50)
    text = models.TextField() # прописать минимальную длину поста
    theme = models.CharField(max_length=30, default="Раздумья")
    post_date = models.DateField(default=timezone.now) # прописать правильную дату
    hash_tags = models.CharField(max_length=15, default="#default")


class HistoryNews(models.Model):
    text = models.TextField(max_length=150)
    date = models.DateField(default=timezone.now)



class DonationPeople(models.Model):
    nickname = models.CharField(max_length=30)
    cash = models.IntegerField()

