from . import views
from django.urls import path

app_name = 'input_form'

urlpatterns = [
    path('', views.home, name='home')
]