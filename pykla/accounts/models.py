from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    tel = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self):
        return '%s - %s - %s' %(self.username, self.first_name, self.tel)

# method creating user profile. Uses django signal to save user after being created
def create_profile(sender, **kwargs ):
   if kwargs['created']:
       UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

