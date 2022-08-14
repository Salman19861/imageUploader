from django.contrib import admin
from .models import imgModel
# Register your models here.
@admin.register(imgModel)
class imgModelAdmin(admin.ModelAdmin):
    list_display=['id','img','date']