from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today)


class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='img', null=True, blank=True)
    due = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    TOOL_STATUS = (
        ('m', 'Maintenance'),
        ('r', 'Reserved'),
        ('c', 'Checked out'),
        ('a', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=TOOL_STATUS,
        blank=True,
        default='a',
    )

    @property
    def is_overdue(self):
        if self.due and datetime.date.today() > self.due:
            return True
        return False

    class Meta:
        ordering = ['due']

    def __str__(self):
        return self.name


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    tools = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True,)
#
#
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#
#
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
