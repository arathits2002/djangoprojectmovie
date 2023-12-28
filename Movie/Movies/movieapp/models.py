from django.db import models

# Create your models here.

class addmodel(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to='movieimg/movie',null=True,blank=True)
    def __str__(self):
        return self.title