import json
from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import app
from app.exceptions.exceptions import RoleNotFoundException, RoleAlreadyExistsException
from tests.responses.responses_views import *


class TestRoleViews(TestCase):
    def setUp(self):
        self.app = app.create_app(start_orm=False).test_client()
        self.app.testing = True

    def test_ping(self):
        result = self.app.get("role/ping")
        self.assertEqual(PONG_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_controller.get_role_by_id")
    def test_get_role_by_id_OK(self, role_mock):
        role_mock.return_value = ROLE_OK_SCOPES_RESPONSE

        result = self.app.get(f"role/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_OK_SCOPES_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_controller.get_role_by_id")
    def test_get_role_by_id_NOT_FOUND(self, role_mock):
        role_mock.side_effect = RoleNotFoundException(VALID_ROLE_ID)

        result = self.app.get(f"role/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_NOT_FOUND_ID_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)

    @patch("app.role_controller.get_role_by_name")
    def test_get_role_by_name_OK(self, role_mock):
        role_mock.return_value = ROLE_OK_SCOPES_RESPONSE

        result = self.app.get(f"role/name/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_OK_SCOPES_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_controller.get_role_by_name")
    def test_get_role_by_name_NOT_FOUND(self, role_mock):
        role_mock.side_effect = RoleNotFoundException(VALID_ROLE_NAME)

        result = self.app.get(f"role/name/{VALID_ROLE_NAME}")
        self.assertEqual(ROLE_NOT_FOUND_NAME_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)

    @patch("app.role_controller.create_role")
    def test_create_role_CREATED_no_scopes(self, role_mock):
        role_mock.return_value = ROLE_OK_NO_SCOPES_RESPONSE

        result = self.app.post("role/", data=json.dumps(ROLE_OK_NO_SCOPES_RESPONSE))
        self.assertEqual(ROLE_OK_NO_SCOPES_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.CREATED, result.status_code)

    @patch("app.role_controller.create_role")
    def test_create_role_CREATED_scopes(self, role_mock):
        role_mock.return_value = ROLE_OK_SCOPES_RESPONSE

        result = self.app.post("role/", data=json.dumps(ROLE_OK_SCOPES_RESPONSE))
        self.assertEqual(ROLE_OK_SCOPES_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.CREATED, result.status_code)

    @patch("app.role_controller.create_role")
    def test_create_role_CONFLICT(self, role_mock):
        role_mock.side_effect = RoleAlreadyExistsException(VALID_ROLE_NAME)

        result = self.app.post("role/", data=json.dumps(ROLE_OK_SCOPES_RESPONSE))
        self.assertEqual(ROLE_ALREADY_EXISTS_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.CONFLICT, result.status_code)
