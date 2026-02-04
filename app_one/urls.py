from django.urls import path
from . import views

app_name = 'app_one'

urlpatterns = [
    path('', views.page_one, name='page_one'),
]