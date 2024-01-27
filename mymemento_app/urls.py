from django.urls import path,include
from mymemento_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-memento/', views.addMemento, name='add-memento'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.signin, name='login'),
    path('memento/<int:id>', views.memento, name='memento'),
]