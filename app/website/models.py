from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Currency(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    date_achieved = models.DateField(null=True)
    description = models.TextField(null=True)
    avatar = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(User, max_length=150)
    email = models.CharField(User, max_length=100)
    currencies = models.ManyToManyField(Currency)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} Profile'


