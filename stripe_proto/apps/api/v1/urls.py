""" API v1 URLs. """
from django.urls import path
from .views import create_stripe_customer, create_stripe_subscription


app_name = 'v1'
urlpatterns = [
    path('create-stripe-customer/', create_stripe_customer),
    path('create-stripe-subscription/', create_stripe_subscription),
]
