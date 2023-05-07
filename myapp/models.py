from django.db import models

# Create your models here.
class Detail(models.Model):
   username=models.CharField(max_length=100)
   image=models.ImageField(upload_to='images/')
   status=models.CharField(max_length=100 ,default='active')
   
   def __str__(self):
      return self.username
   