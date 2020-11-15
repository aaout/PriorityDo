from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update/<str:pk>/', views.updateTodo, name="update_todo"),
    path('delete/<str:pk>/', views.deleteTodo, name="delete"),
    path('sort_importance', views.sort_importance, name="sort_importance"),
    path('sort_motivation', views.sort_motivation, name="sort_motivation"),
    path('sort_progress', views.sort_progress, name="sort_progress"),
]
