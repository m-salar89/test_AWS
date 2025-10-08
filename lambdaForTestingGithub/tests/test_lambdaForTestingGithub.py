import json
import pytest
import boto3
import os


import sys
sys.path.append("src")
from lambda_function import lambda_handler


def dateipytestTesten():

    event = {"request": {"userAttributes": {"sub": "user-missing-env"}}}

    result = lambda_handler(event, None)
    print(result)

    assert result == event