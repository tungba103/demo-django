from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('permissions', PermissionViewSet)
urlpatterns = router.urls