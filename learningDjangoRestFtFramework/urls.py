from django.urls import path
from . import views # from the current path import views

urlpatterns = [
    path('allUsers/', views.UsersView.as_view(), name='users'),
    path('user/', views.UserDetailView.as_view(), name='user-detail'),
    path('rest/delete_user/', views.delete_user),
    path('sequences/', views.Sequences.as_view(), name='sequences'),
]
