from django.urls import path 
from . import views


app_name = 'courses'

urlpatterns = [
    path('' , views.subject_courses_list , name='subject_course_list'),
    path('course/<slug:slug>/' , views.course_detail , name='course_detail')

]

