from rest_framework import serializers

from .models import NavigationLink


class NavigationLinkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = NavigationLink
