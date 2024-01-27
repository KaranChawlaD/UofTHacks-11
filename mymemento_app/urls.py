from django.urls import path,include
from mymemento_app import views

urlpatterns = [
    path('', views.index, name="index",),
]