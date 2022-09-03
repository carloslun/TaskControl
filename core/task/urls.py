from django.urls import path
from .views import LoginView

# app_name = "task"
urlpatterns = [
    path('', LoginView.as_view(), name = "createLoginView"),
    
    #crar mas url pathbase = /api/
]