from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    genre_choices = (
        ('Sci-fi', 'Sci-fi'),
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
    )
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=25, choices=genre_choices)
    director = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return self.title 

class Profile(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    address = models.TextField()

    def __unicode__(self):
        return self.user 

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
