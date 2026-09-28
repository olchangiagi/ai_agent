'''
bedrock runtime client 획득 코드 (Colab 참조)
'''
import boto3
from .config import AWS_REGION

def runtime_client():
    return boto3.client(service_name = 'bedrock-runtime', region_name = AWS_REGION)