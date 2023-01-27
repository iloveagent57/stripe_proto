from django.db import models

from stripe_proto.apps.core.models import TimeStampedModelWithUuid


class Subscription(TimeStampedModelWithUuid):
    """
    Represents a generic subscription.  But it's concrete.
    Child classes like ``StripeSubscription`` will exist.
    """

