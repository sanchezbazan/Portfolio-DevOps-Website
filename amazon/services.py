# services.py
from .models import AWSCostData
from .utils import get_aws_client

'''
1. Business Logic: Functions or classes here encapsulate the core business operations of your application. They operate on data models and may execute tasks such as processing data, handling complex calculations, or interacting with external APIs.
2. Database Interactions: Services often deal with reading from or writing to your database. They use models to fetch, update, or persist data.
3. Integration Logic: If your application integrates with external services (like sending emails, fetching data from external APIs), the code handling this communication might reside here, especially if it involves complex logic beyond simple HTTP calls.
'''

def fetch_and_store_aws_data(query):
    try:
        client = get_aws_client()
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': query.start_date.strftime("%Y-%m-%d"),
                'End': query.end_date.strftime("%Y-%m-%d")
            },
            Granularity=query.granularity,
            GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}, {"Type": "TAG", "Key": "Environment"}],
            Metrics=["BlendedCost", "UnblendedCost", "UsageQuantity"]
        )
        for result in response['ResultsByTime']:
            for group in result['Groups']:
                AWSCostData.objects.create(
                    query=query,
                    date=result['TimePeriod']['Start'],
                    service=group['Keys'][0],
                    environment=group['Keys'][1] if len(group['Keys']) > 1 else None,
                    blended_cost=float(group['Metrics']['BlendedCost']['Amount']),
                    unblended_cost=float(group['Metrics']['UnblendedCost']['Amount']),
                    usage_quantity=float(group['Metrics']['UsageQuantity']['Amount'])
                )
    except ClientError as e:
        logger.error(f"ClientError from AWS: {e.response['Error']['Message']}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")