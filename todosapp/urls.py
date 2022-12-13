from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homePage"),
    path('newTodo/', views.newTodo, name="newTodo"),
    path('editTodo/', views.editTodo, name="editTodo"),
    path('removeTodo/<int:id>', views.removeTodo, name="removeTodo"),
]
