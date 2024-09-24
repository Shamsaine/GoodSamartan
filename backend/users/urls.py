from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView

urlpatterns = [
    # JWT login for obtaining and refreshing tokens
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom registration and login views
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/custom-login/', LoginView.as_view(), name='custom_login'),
]
