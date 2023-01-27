from django.db import models

from stripe_proto.apps.core.models import TimeStampedModelWithUuid, User
from stripe_proto.apps.backends.models import Subscription



class BaseCustomerSubscription(TimeStampedModelWithUuid):
    """
    An account that will be associated with a subscription.
    """
    class Meta:
        abstract = True

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    subscription = models.ForeignKey(
        Subscription, null=True, blank=True, on_delete=models.CASCADE,
        help_text="The account's Subscription object, if it exists"
    )


class IndividualSubscription(BaseCustomerSubscription):
    """
    An account that will be associated with a subscription.
    """


class TeamSubscription(BaseCustomerSubscription):
    """
    An account with an owner and 1 or more team members.
    """
    members = models.ManyToManyField(
        User,
        related_name='team_accounts',
        through='TeamMembership',
    )


class TeamMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_account = models.ForeignKey(TeamSubscription, on_delete=models.CASCADE)
