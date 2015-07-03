from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=50,default="")
    age = models.CharField(null=True,max_length=50)
    image = models.ImageField(upload_to='team/',null=True,default="")

    def __unicode__(self):
      return self.name


class Adopt(models.Model):
    animal = models.OneToOneField(Animal)
    description = models.CharField(max_length=500,default="")

    def __unicode__(self):
      return self.animal.name

class Story(models.Model):
    animal = models.OneToOneField(Animal)
    description = models.CharField(max_length=500,default="")

    def __unicode__(self):
      return self.animal.name

