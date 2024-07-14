from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    path("clicker/", views.index),
    path('store/', views.store),
    path('rating/', views.rating),
    path('profile/', views.profile),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)