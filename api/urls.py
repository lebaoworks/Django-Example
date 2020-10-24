from django.urls import include, path
from api import views

urlpatterns = [
    path('api', views.ListAPIs.as_view()),
]