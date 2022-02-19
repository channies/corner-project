from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup.as_view()),
]