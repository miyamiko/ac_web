from django.urls import path
from . import views

app_name    = "ac_app"
urlpatterns = [ 
    path('', views.AccessView.as_view(), name="index"),
]