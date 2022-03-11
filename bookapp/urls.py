from django.contrib import admin
from django.urls import path
from bookapp import views

urlpatterns = [
    path('', views.book_list),
    path('list/', views.book_list),
    path('add/', views.book_add),
    path('edit/<int:nid>/', views.book_edit),
    path('delete/', views.book_delete),
    path('search/', views.book_search),
]