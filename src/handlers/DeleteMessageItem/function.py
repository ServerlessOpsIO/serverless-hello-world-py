'''Put item in DDB'''
import json
import logging
import os

import boto3


# This path reflects the packaged path and not repo path to the common
# package for this service.
import common   # pylint: disable=unused-import

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

DDB_TABLE_NAME = os.environ.get('DDB_TABLE_NAME')
ddb_res = boto3.resource('dynamodb')
ddb_table = ddb_res.Table(DDB_TABLE_NAME)


def _delete_item(item: dict) -> dict:
    '''Delete item in DDB'''
    r = ddb_table.delete_item(
        Key={
            'pk': item.get('message_id'),
            'sk': 'v0'
        },
    )
    return r


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))
    message = json.loads(event['Records'][0]['Sns']['Message'])

    resp = _delete_item(message)

    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

