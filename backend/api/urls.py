from django.urls import path
from .views import GenerateText

urlpatterns=[
    path("generate/",GenerateText.as_view())
]