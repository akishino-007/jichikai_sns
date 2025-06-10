from django.db import models
from django.contrib.auth.models import User

from .consts import MAX_RATE


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE+1)]

# Create your models here.

CATEGORY = (('kairan','回覧板'),('keiji','掲示板'),('osirase','お知らせ'))

class Info(models.Model):
    category = models.CharField(
        max_length=50,
        choices = CATEGORY
        )
    title = models.CharField(max_length=250,verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')    
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        verbose_name='投稿日'
        )
    thumbnail1 = models.ImageField(null=True, blank=True)
    thumbnail2 = models.ImageField(null=True, blank=True)
    thumbnail3 = models.ImageField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)  # ファイルをアッ
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    title = models.ForeignKey(Info, on_delete=models.CASCADE,
        max_length=250,
        verbose_name='タイトル',
        related_name="title_reviews"
        )
    text = models.TextField(verbose_name='コメント')    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title.title
