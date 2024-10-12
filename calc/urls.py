from django.urls import path
from . import views # from the current path import views

urlpatterns = [
    path('', views.root, name='root'),
    path('home/', views.home, name='home'),
    path('users/', views.getAllUsers, name='getAllUsers'),
    path('insertUser/', views.insertUser, name='insertUser'),
    path('handle_get_request/', views.handle_get_request, name='handle_get_request'),
    path('handle_post_request/', views.handle_post_request, name='handle_post_request'),
    path('test/', views.test_view, name="test_view"),
]
