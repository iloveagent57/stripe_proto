from django.contrib import admin

from .models import IndividualSubscription


@admin.register
class IndividualSubscriptionAdmin(admin.ModelAdmin):
    """
    """
    class Meta:
        fields = '__all__'
