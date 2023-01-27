"""
Models for very simple Stripe Subscription object(s).
"""
from django.db import models

from ..base.models import Subscription


# Create your models here.

class StripeSubscription(Subscription):
    """
    Holds the most minimal information about a Stripe subscription.
    """
    identifier = models.CharField(
        max_length=255,
        null=False,
        unique=True,
    )
