from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    video_no = models.AutoField
    video_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    video_thumbnail = models.ImageField(upload_to='website/images',default="")
    pub_date = models.DateField(default=timezone.now)
    url =models.CharField(max_length=100,default="https://www.youtube.com/channel/UC0Ld6EqhdyQ3xiEtg1fKQXg?view_as=subscriber")
    def  __str__(self):
        return self.video_name
class Message(models.Model):
    mess_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=15,default="")
    desc = models.CharField(max_length=1500,default="")

    def  __str__(self):
        return self.name