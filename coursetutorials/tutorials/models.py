from django.db import models


    

class TutorialSeries(models.Model):
    series_title = models.CharField(max_length=120, blank=False)
    series_desc = models.TextField()
    # series_thumbnail =
    # series_tags =
    
    def __str__(self):
        return self.series_title




# Create your models here.
class Tutorial(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, blank=False)
    desc = models.TextField()
    video_url = models.CharField(max_length=150)
    # https://stackoverflow.com/questions/22340258/list-field-in-model
    # https://django-mysql.readthedocs.io/en/latest/model_fields/list_fields.html
    # tags =
    individual = models.BooleanField(default=True)  # SET TRUE IF IT IS SERIES
    series = models.ForeignKey(TutorialSeries, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        if self.series == None:
            self.individual = True
        else:
            self.individual = False

        super(Tutorial, self).save(*args, **kwargs)

    def __str__(self):
        return self.title