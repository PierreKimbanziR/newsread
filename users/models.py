from django.db import models
from django.contrib.auth.models import User
from .API_CALL import get_sources_list 
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user.username} Profile'



# Creating the model for the media selection, using the News Api source list

list_of_choices = get_sources_list()

class MediaList(models.Model):
    medias = MultiSelectField(choices=list_of_choices)
    user = models.ForeignKey(User, default = User, on_delete=models.CASCADE)







