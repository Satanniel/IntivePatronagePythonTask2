from django.urls import path

from . import views

app_name = 'salaries'
urlpatterns = [
    path('', views.salaries, name='salaries'),
]
