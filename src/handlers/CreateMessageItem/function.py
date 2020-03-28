'''Put item in DDB'''
import json
import logging
import os

# AWS X-RAY
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
# Only instrument libraries if not running locally
if "AWS_SAM_LOCAL" not in os.environ:
    patch_all()


# This path reflects the packaged path and not repo path to the common
# package for this service.
import common   # pylint: disable=unused-import

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

def handler(event, context):
    '''Function entry'''
    _logger.debug('Event: {}'.format(json.dumps(event)))

    resp = {}

    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

