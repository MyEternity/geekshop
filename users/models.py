from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

NULL_INSTALL = {'null': True, 'blank': True}


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=18)

    activation_key = models.CharField(max_length=128, blank=True, null=True)
    # activation_key_created = models.DateTimeField(default=(now()+timedelta(hours=48)))
    activation_key_created = models.DateTimeField(auto_now_add=True, **NULL_INSTALL)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_created + timedelta(hours=48):
            return False
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='Теги', max_length=128, blank=True)
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    gender = models.CharField(verbose_name='Пол', choices=GENDER_CHOICES, blank=True, max_length=5)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
