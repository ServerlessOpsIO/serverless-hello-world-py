'''Put item in DDB'''
import json
import logging
import os

from datetime import datetime
from uuid import uuid4
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


def _put_ddb_item(item: dict) -> dict:
    '''Put item into DDB'''
    r = ddb_table.put_item(
        Item=item
    )
    return r


def _create_item(item: dict) -> dict:
    '''Transform item to put into DDB'''
    dt = datetime.utcnow()
    dt_ttl = dt.replace(year=dt.year + 1)
    item['pk'] = str(uuid4())
    item['timestamp'] = int(dt.timestamp())
    item['ttl'] = int(dt_ttl.timestamp())

    return _put_ddb_item(item)


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))
    message = json.loads(event['Records'][0]['Sns']['Message'])

    resp = _create_item(message)

    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

