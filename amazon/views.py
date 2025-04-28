from django.shortcuts import render
import boto3
from django.http import JsonResponse
from datetime import datetime, timedelta
from .variables import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
# Create your views here.

def get_aws(request):

    start_date = datetime(datetime.now().year, 3, 1)  # March 1st
    end_date = datetime(datetime.now().year, 3, 31)   # March 31st

    client = boto3.client(
        'ce',  # Cost Explorer
        aws_access_key_id= AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.strftime("%Y-%m-%d"),
            'End': end_date.strftime("%Y-%m-%d")
        },
        Granularity='MONTHLY',
        GroupBy =[
                    {
                    "Type":"DIMENSION",
                    "Key":"SERVICE"
                    },
                    {
                    "Type":"TAG",
                    "Key":"Environment"
                    }
        ],
        Metrics = ["BlendedCost", "UnblendedCost", "UsageQuantity"]


    )

    results = []
    for result in response['ResultsByTime']:
        date = result['TimePeriod']['Start']
        for group in result['Groups']:
            service = group['Keys'][0]  # SERVICE name
            environment = group['Keys'][1] if len(group['Keys']) > 1 else None  # Environment tag (optional)
            blended_cost = float(group['Metrics']['BlendedCost']['Amount'])
            unblended_cost = float(group['Metrics']['UnblendedCost']['Amount'])
            usage_quantity = float(group['Metrics']['UsageQuantity']['Amount'])

            results.append({
                'date': date,
                'service': service,
                'environment': environment,
                'blended_cost': blended_cost,
                'unblended_cost': unblended_cost,
                'usage_quantity': usage_quantity
            })


    
    return JsonResponse({'data': results})