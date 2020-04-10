from django.urls import path
from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_user', views.create_user, name='create_user')
]