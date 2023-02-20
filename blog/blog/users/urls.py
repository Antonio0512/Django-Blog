from django.urls import path

from blog.users import views

urlpatterns = [
    path('', views.register, name='register')
]