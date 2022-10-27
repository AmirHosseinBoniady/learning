from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('cars/', views.cars_detail),
]
