from django.urls import path

from . import views

app_name = 'packages'

urlpatterns = [
    path('', views.add, name='addpackage'),
]