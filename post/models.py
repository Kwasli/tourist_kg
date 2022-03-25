from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField('название', max_length=100)
    slug = models.SlugField(max_length=100)
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    def __str__(self):
        return self.name
        



class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to = "post/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField('Активный', default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        
    def __str__(self):
        return self.title

class Comment(models.Model):

    name = models.CharField("имя", max_length=50)
    comment = models.TextField("Коментарий")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)