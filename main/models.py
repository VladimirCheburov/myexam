from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class vcexam(models.Model):
    name = models.CharField('Название экзамена', max_length=255)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    exam_date = models.DateField('Дата проведения экзамена')
    image = models.ImageField('Задание (картинка)', upload_to='exam_images/', blank=True, null=True)
    users = models.ManyToManyField(User, verbose_name='Пользователи')
    is_public = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.name
