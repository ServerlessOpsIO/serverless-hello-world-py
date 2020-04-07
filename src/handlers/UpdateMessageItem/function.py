'''Update item in DDB'''
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


def _update_item(item: dict) -> dict:
    '''Update item in DDB'''
    message_id = item.pop('message_id')

    attribute_updates = {}
    for key in item.keys():
        attribute_updates[key] = {'Action': 'PUT', 'Value': item.get(key)}

    r = ddb_table.update_item(
        Key={
            'pk': message_id
        },
        AttributeUpdates=attribute_updates
    )
    return r


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))
    message = json.loads(event['Records'][0]['Sns']['Message'])

    resp = _update_item(message)

    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

