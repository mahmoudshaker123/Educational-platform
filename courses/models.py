from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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
    



class content(models.Model):
    module = models.ForeignKey(Module , related_name='contents' , on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType ,on_delete=models.CASCADE , limit_choices_to={'model__in':('text' ,'file' ,'image' , 'video' )})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model):
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,  
        related_name='%(class)s_related'
    )
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title)


class Text(ItemBase):
    text = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    image = models.FileField(upload_to='images')

class Video(ItemBase):
    video = models.URLField()
