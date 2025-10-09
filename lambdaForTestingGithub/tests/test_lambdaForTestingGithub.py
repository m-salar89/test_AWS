import json
import pytest
import boto3
import os


import sys
sys.path.append("src")
from lambda_function import lambda_handler


def test_dateipytestTesten():

    event = {'statusCode': 200,
        'body': json.dumps('dieser änderung ist für testen des workflows!')}

    result = lambda_handler(event, None)
    print(result)

    assert result == event