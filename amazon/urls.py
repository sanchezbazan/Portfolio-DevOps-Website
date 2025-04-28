from django.urls import path
from .views import get_aws

urlpatterns = [
    path('buckets/', get_aws, name='aws_buckets'),
]
