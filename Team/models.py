from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400,default="")
    image = models.ImageField(upload_to='team/',null=True,default="")

    def __unicode__(self):
      return self.name