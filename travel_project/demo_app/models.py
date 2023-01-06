from django.db import models

# Create your models here.
class travel(models.Model):
    place=models.CharField(max_length=250)
    img=models.ImageField(upload_to='photo')
    about=models.TextField()

    def __str__(self):
        return self.place
class team(models.Model):
    surname=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.surname