from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('list_users/', views.list_users, name='list_users'),
    path('create_expense/', views.create_expense, name='create_expense'),
    path('list_expenses/', views.list_expenses, name='list_expenses'),
    path('', views.expenses_home, name='expenses_home'),  # Add this line
]
