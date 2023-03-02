from django.urls import path, include
from .api_views import(
    PetApiView,
)

urlpatterns=[
    path('pets/', PetApiView.as_view()),
    path('pets/<int:pk>', PetApiView.as_view()),    
]