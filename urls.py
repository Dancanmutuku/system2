from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("leave", views.leave, name="leave"),
    path("custom_logout", views.custom_logout, name="custom_logout"),
    path("", include("django.contrib.auth.urls")), 
]