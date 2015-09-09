from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from others.mjango.field import filter_kwargs

class UserManager(BaseUserManager):
    def create(self, **kwargs):
        filtered_args = filter_kwargs(self.model, kwargs)
        user = self.model(**filtered_args) # date of birth 'YYYY-MM-DD' format
        user.set_password(filtered_args['password'])
        user.save()


class User(AbstractBaseUser):
    contact = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=15, null=True)
    nickname = models.CharField(max_length=15, null=True)
    avatar = models.CharField(max_length=150, null=True)
    date_of_birth = models.DateField(null=True)
    #
    friend = models.ManyToManyField('self')
    friend_request = models.ManyToManyField('self',  symmetrical=False,  related_name='fr')
    #
    objects = UserManager()
    USERNAME_FIELD = 'contact'


class Token(models.Model):
    token = models.CharField(max_length=150)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)