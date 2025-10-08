import json
import pytest
import boto3
import os


import sys
sys.path.append("src")
from lambda_function import lambda_handler


def test_dateipytestTesten():

    event = {{'body': '"Hello from Lambda!"', 'statusCode': 200}}

    result = lambda_handler(event, None)
    print(result)

    assert result == event