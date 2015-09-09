from django.db import models
from django.conf import settings

class Extra(models.Model):
    kind = models.CharField(max_length=15)
    url = models.CharField(max_length=100)


class Square(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    extra = models.OneToOneField(Extra, null=True)
    title = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    paragraph = models.TextField(null=True)
    active = models.NullBooleanField(default=True)


class DeliverySquare(models.Model):
    square = models.ForeignKey(Square)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL)


class EverNoteAuthTrack(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    oauth_token = models.CharField(max_length=1000, null=True)
    oauth_token_secret = models.CharField(max_length=1000, null=True)
    oauth_verifier = models.CharField(max_length=1000, null=True)


