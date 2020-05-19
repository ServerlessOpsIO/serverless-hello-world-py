'''Get item from DDB'''
import json
import logging
import os

import boto3

# This path reflects the packaged path and not repo path to the common
# package for this service.
from common.dynamodb import DecimalEncoder

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

DDB_TABLE_NAME = os.environ.get('DDB_TABLE_NAME')
ddb_res = boto3.resource('dynamodb')
ddb_table = ddb_res.Table(DDB_TABLE_NAME)


def _retrieve_item(message_id: str) -> dict:
    '''Get item in DDB'''
    r = ddb_table.get_item(
        Key={
            'pk': message_id,
            'sk': 'v0'
        }
    )
    _logger.debug('DDB Get response: {}'.format(r))
    item = r.get('Item', {})
    item['message_id'] = item.pop('pk')

    return item


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))
    message_id = event['pathParameters']['message_id']

    item = _retrieve_item(message_id)

    resp = {
        "statusCode": 200,
        "body": json.dumps(item, cls=DecimalEncoder)
    }

    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp


