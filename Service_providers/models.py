from django.db import models

# from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class ServiceProvider(models.Model):
        user            = models.OneToOneField(User)
        phone_number        = models.CharField(max_length=12,default="+233")
        name            = models.CharField(max_length=100)
        picture = models.ImageField(upload_to='profile_images', blank=True)

        def __unicode__(self):
                return self.name