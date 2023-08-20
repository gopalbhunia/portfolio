from django.db import models

# Create your models here.
#-----Contact Table Model here---------
class Contact(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField()
    phonenumber= models.CharField(max_length=12)
    description= models.TextField() 
    
    
    def __str__(self):
        return self.name


#  -----Blog Table Model here---
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    authname = models.CharField(max_length=20)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
# ------Project Table Model here-------
class Project(models.Model):
    projectName = models.CharField(max_length=50)
    projectDescription = models.TextField()
    projectTimestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return self.projectName 
    
# ----Skill Table Model Here------
class skillupdate(models.Model):
    skillName = models.TextField()
    
    def __str__(self):
        return self.skillName
    