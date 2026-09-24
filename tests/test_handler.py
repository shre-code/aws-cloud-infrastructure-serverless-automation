import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).parents[1] / "lambda"))

import handler


def test_health():
    result = handler.lambda_handler(
        {"requestContext": {"http": {"method": "GET"}}, "rawPath": "/health"},
        None,
    )
    assert result["statusCode"] == 200


def test_create_item():
    handler.table = MagicMock()
    result = handler.lambda_handler(
        {
            "requestContext": {"http": {"method": "POST"}},
            "rawPath": "/items",
            "body": '{"name": "demo"}',
        },
        None,
    )
    assert result["statusCode"] == 201
    handler.table.put_item.assert_called_once()


def test_missing_item():
    handler.table = MagicMock()
    handler.table.get_item.return_value = {}
    result = handler.lambda_handler(
        {
            "requestContext": {"http": {"method": "GET"}},
            "rawPath": "/items/123",
        },
        None,
    )
    assert result["statusCode"] == 404
