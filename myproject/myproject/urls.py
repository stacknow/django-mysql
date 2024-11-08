from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.get_users, name='get_users'),
    path('users/create', views.create_user, name='create_user'),
]
