from rest_framework import routers
from .views import IrisViewSet

router = routers.DefaultRouter()
router.register(r'iris', IrisViewSet)
