from django.db import models
from django.contrib.auth import User
# Create your models here.



class Subject(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250 , unique=True)


    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return str(self.title)   
    

class Course(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'AV' , 'Available'
        DEREFT = 'DF' , 'Dereft'
    owner = models.ForeignKey(User , related_name= 'courses_created' , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , related_name= 'courses' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250 , unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=2 , choices=Status , default=Status.AVAILABLE)


    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return str(self.title)   
    

class Module(models.Model):
    course = models.ForeignKey(Course , related_name='modules' , on_delete=models.CASCADE )
    title = models.CharField(max_length= 250 )
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return str(self.title)   