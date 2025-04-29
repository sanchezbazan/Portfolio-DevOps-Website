# utils.py
import boto3
from .config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

'''
1. Reusable Code: Functions in utils.py are designed to be used by multiple modules throughout your application. They often provide solutions to common problems, like formatting dates, converting units, or validating data.

2. Helper Functions: They simplify tasks and are not directly involved in the business logic or data handling specific to your application's domain. For example, a function to merge two dictionaries or to send an email with a pre-defined template.

3. No Side Effects: Utilities generally do not cause side effects in the database or other parts of the system. They take inputs, process them, and return results.

4. No Dependencies: They are often self-contained and do not rely on the state of the application or external services. This makes them easier to test and reuse.
'''
# This function creates an AWS Cost Explorer client using the provided credentials and region.
def get_aws_client():
    return boto3.client(
        'ce',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
