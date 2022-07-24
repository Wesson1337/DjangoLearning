from rest_framework import routers
from rest_app.api import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
