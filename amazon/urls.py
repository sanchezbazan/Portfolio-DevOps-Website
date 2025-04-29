from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AWSCostQueryViewSet, AWSCostDataViewSet

router = DefaultRouter()
router.register(r'cost-queries', AWSCostQueryViewSet)
router.register(r'cost-data', AWSCostDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
