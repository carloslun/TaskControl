from django.urls import path
from .views import UserView

urlpatterns = [
    path('', UserView.as_view(), name = "ListCreateUser"),
    
    #crear mas url pathbase = /api/
]