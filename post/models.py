from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Post(models.Model):


   user= models.ForeignKey('post.ProfileUser', on_delete=models.CASCADE, verbose_name='Имя пользователь')
   title= models.CharField(max_length=55, verbose_name= 'Название поста')
   description = models.TextField(verbose_name='Oписание поста')
   image=models.ImageField(upload_to='post_image/', verbose_name='фото публикации')
   created =models.DateTimeField(verbose_name='Дата пупликации поста',auto_now_add=True)

   class Meta:
      verbose_name = 'Посты'
      verbose_name_plural = 'Посты'

   def __str__(self) -> str:
      return f'{self.title} - {self.created}'


class ProfileUser(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователь')
    profile_image =models.ImageField(upload_to='user/profile_image/', verbose_name='аватарка')




