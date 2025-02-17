from django.db import models

# Create your models here.

# 用户id，用户名username，手机号phone，密码password，邮箱email，照片image

class RegisterUser(models.Model):
    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False, unique=True)
    phone = models.CharField(max_length=20, blank=False, unique=True)
    email = models.CharField(max_length=20, blank=False, unique=True)
    image = models.ImageField(upload_to='image/',blank=True,null=True)



class Meta:
    managed = True
    db_table = 'RegisterUser'