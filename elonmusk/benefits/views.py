from rest_framework import viewsets

from .models import Benefit
from .serializers import BenefitSerializer


class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer
