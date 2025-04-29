from rest_framework import serializers
from .models import AWSCostQuery, AWSCostData

class AWSCostQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSCostQuery
        fields = '__all__'

class AWSCostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSCostData
        fields = '__all__'
