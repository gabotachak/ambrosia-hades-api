from http import HTTPStatus
from unittest import TestCase

import app
from tests.responses.responses_views import PONG_RESPONSE


class TestPingViews(TestCase):
    def setUp(self):
        self.app = app.create_app(start_orm=False).test_client()
        self.app.testing = True

    def test_ping(self):
        result = self.app.get("/ping")
        self.assertEqual(PONG_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)
