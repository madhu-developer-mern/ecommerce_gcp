from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, CurrentUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('me/', CurrentUserView.as_view(), name='current-user'),
]
