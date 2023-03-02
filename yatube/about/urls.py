from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('author/', views.AboutAuthorView.as_view(), name='autor'),
    path('tech/', views.AboutTechView.as_view(), name='tech'),
]
