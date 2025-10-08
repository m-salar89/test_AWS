import json
import pytest
import boto3


import sys
sys.path.append("src")
from lambda_funktion import lambda_handler


def dateipytestTesten():

    event = {"request": {"userAttributes": {"sub": "user-missing-env"}}}

    result = lambda_handler(event, None)

    assert result == event