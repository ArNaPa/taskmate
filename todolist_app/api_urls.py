from rest_framework import routers
from .api import TaskViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('', TaskViewSet, 'api_urls')

urlpatterns = router.urls
