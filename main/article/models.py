from datetime import timezone

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256, unique=True)
    mini_description = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, verbose_name='Картинка')

'''    def __str__(self):
        return self.description'''


'''class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now, null=True)'''

