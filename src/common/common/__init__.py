'''Common code for DDB'''
from decimal import Decimal
from json import JSONEncoder

class DecimalEncoder(JSONEncoder):
    '''Convert decimal values returned by boto3 DDB deserializer'''
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


