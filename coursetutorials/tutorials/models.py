from django.db import models

# Create your models here.
class Tutorial(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, blank=False)
    desc = models.TextField()
    video_url = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title