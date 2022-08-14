from django.db import models

# Create your models here.
class imgModel(models.Model):
    img=models.ImageField(upload_to='allImages')  #ab iss name ka aik folder uss mei saray imgs save hongai.
    #img field k sath km krnay k liye pillow ka install hona xrori hai.
    #agr model form mei widget dena hia to iss ka field ClearableFileInput hoga.
    date=models.DateTimeField(auto_now=True)
    