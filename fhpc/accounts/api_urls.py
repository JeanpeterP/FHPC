from django.urls import path
from .api_views import(
    AccountListApiView,
    CustomTokenObtainPairView
)

urlpatterns=[
    #path("accounts/", api_accounts, name="api_salespersons")
    path('accounts/', AccountListApiView.as_view()),
    path('accounts/<int:pk>', AccountListApiView.as_view()),  
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenObtainPairView.as_view(),name='token_refresh'),
]