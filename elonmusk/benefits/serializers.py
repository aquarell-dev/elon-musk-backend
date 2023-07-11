from rest_framework import serializers

from .models import Benefit


class BenefitSerializer(serializers.ModelSerializer):
    benefit = serializers.SerializerMethodField()

    def get_benefit(self, instance: Benefit):
        return {
            'top': instance.top,
            'middle': instance.middle,
            'bottom': instance.bottom,
        }

    class Meta:
        fields = ['id', 'benefit']
        model = Benefit
