from django.urls import path
from . import views

urlpatterns = [
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('marks/', views.marks, name='marks'),
    path('scores/', views.score, name='score'),
    path('personaldetails/', views.personaldetails, name='personaldetails'),

]
