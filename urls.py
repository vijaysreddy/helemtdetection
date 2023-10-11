from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image_upload/', views.image_upload, name = 'image_upload'),
    path('view_images/', views.view_images, name = 'view_images'),
]