from django.urls import path
from .views import CartInfoView

urlpatterns = [
    path('info/', CartInfoView.as_view(), name='cart-info'),
]
