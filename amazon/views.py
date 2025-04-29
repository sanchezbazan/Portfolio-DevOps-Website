from django.http import JsonResponse
from .utils import get_aws_client
from .services import fetch_and_store_aws_data
from rest_framework import viewsets, permissions
from .models import AWSCostQuery, AWSCostData
from .serializers import AWSCostQuerySerializer, AWSCostDataSerializer
import boto3
import logging
from django.conf import settings
from botocore.exceptions import ClientError

class AWSCostQueryViewSet(viewsets.ModelViewSet):
    queryset = AWSCostQuery.objects.all()
    serializer_class = AWSCostQuerySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        instance = serializer.save()
        fetch_and_store_aws_data(instance)


class AWSCostDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AWSCostData.objects.all()
    serializer_class = AWSCostDataSerializer
    permission_classes = [permissions.AllowAny]
