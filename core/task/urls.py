from django.urls import path
from .views import LoginDetail

app_name = "task"
urlpatterns = [
    path("", LoginDetail.as_view(), name = "createLoginView")
]
