from rest_framework.routers import DefaultRouter

from .views import NavigationLinkViewSet

router = DefaultRouter()

router.register('links', NavigationLinkViewSet)

urlpatterns = router.urls
