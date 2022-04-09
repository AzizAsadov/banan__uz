from django.urls import reverse
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Catigories"

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])
    
    def __str__(self):
        return self.title


class Province(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = "Provinces"

    def get_absolute_url(self):
        return reverse('province', args=[self.slug])

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    date = models.DateField()
    views = models.IntegerField(default=0)
    audio = models.FileField(upload_to='audios/')
    text = models.TextField()
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    province = models.ForeignKey(Province, on_delete = models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title