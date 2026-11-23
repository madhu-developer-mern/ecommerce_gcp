from django.urls import path
from .views import CreateOrderView, MyOrdersView

urlpatterns = [
    path('', CreateOrderView.as_view(), name='create-order'),
    path('my-orders/', MyOrdersView.as_view(), name='my-orders'),
]
