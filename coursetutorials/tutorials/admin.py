from django.contrib import admin
from .models import Tutorial, TutorialSeries

# Register your models here.
admin.site.register(TutorialSeries)
admin.site.register(Tutorial)
