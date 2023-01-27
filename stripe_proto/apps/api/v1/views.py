# Create your views here.
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import authentication, permissions

import djstripe.settings as djstripe_settings
import stripe

from django.contrib.auth.models import User


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_stripe_customer(request):
    return Response({
        'message': 'Customer created.',
        'request_data': request.data,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_stripe_subscription(request):
    """
    Create a Stripe Customer and Subscription object and map them onto the Account object
    Expects the inbound POST data to look something like this:
    {
        'email': 'foo@bar.com',
        'payment_method': 'pm_1GGgzaIXTEadrB0y0tthO3UH',
        'price_id': 'price_GqvXkzAvxlF0wR',
    }
    """
    request_data = request.data
    email = request_data['email']
    # assert request.user.email == email
    payment_method = request_data['payment_method']
    plan_id = request_data['plan_id']
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    return Response({
        'message': 'Subscription created.',
        'request_data': request_data,
    })
