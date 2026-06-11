from django.urls import path
from .views import *
urlpatterns = [
   path('payment/khalti/initiate/', PaymentAPIView.as_view()),       # order_id
   path('payment/khalti/verify/', PaymentVerifyAPIView.as_view())    # pidx
]
