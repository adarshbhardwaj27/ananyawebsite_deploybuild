from django.db import models
from django.utils import timezone

# Create your models here.
class Videos(models.Model):
    video_no = models.AutoField
    video_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    video_thumbnail = models.ImageField(upload_to='website/images',default="")
    pub_date = models.DateField(default=timezone.now)
    url =models.CharField(max_length=100,default="https://www.youtube.com/channel/UC0Ld6EqhdyQ3xiEtg1fKQXg?view_as=subscriber")
    def  __str__(self):
        return self.video_name