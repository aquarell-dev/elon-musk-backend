from rest_framework.routers import DefaultRouter

from .views import BenefitViewSet

router = DefaultRouter()

router.register('benefits', BenefitViewSet)

urlpatterns = router.urls
