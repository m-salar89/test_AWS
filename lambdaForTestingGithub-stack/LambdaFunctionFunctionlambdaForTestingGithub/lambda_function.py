import json
import os
import pytest



def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hallo from local VS!')
    }
