from rest_framework import viewsets

from .models import NavigationLink
from .serializers import NavigationLinkSerializer


class NavigationLinkViewSet(viewsets.ModelViewSet):
    queryset = NavigationLink.objects.all().order_by('order')
    serializer_class = NavigationLinkSerializer
