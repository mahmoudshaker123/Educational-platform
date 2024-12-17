from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ['title' ,'slug']
    prepopulated_fields = {'slug': ['title']}



class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ['title' , 'subject' ,'created' ,'status']
    list_filter = ['created','subject']
    search_fields= ['title','overview']
    prepopulated_fields = {'slug': ['title']}

    inlines = [ModuleInLine]