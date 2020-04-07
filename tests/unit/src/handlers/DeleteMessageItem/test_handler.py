import json
import pytest

from src.handlers.DeleteMessageItem import handler


@pytest.fixture()
def event():
    '''Return a test event'''
    event_data = {}
    return event_data


def test_lambda_handler(event, mocker):
    '''Call handler'''
    ret = handler(event, "")

    # Add assertions below.

