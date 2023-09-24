from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('abouts/', views.about),
    path('hello/<int:id>', views.hello),
    path('juanmi/<str:username>', views.intro),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task)
    
]