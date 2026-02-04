from django.urls import path
from . import views

app_name = 'app_two'

urlpatterns = [
    path('', views.page_two, name='page_two'),
]