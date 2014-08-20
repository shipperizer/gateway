from django.db import models

# Create your models here.


class Repo(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "Repo: {0}".format(self.name)

class File(models.Model):
    repo = models.ForeignKey(Repo)
    name = models.CharField(max_length=200) 
    path = models.CharField(max_length=400) 
    size = models.IntegerField(default=0)
    url  = models.CharField(max_length=400) 
    
    def __unicode__(self):
        return "File: {0}/{1} |{2}GB|".format(self.path,self.name,self.size)
