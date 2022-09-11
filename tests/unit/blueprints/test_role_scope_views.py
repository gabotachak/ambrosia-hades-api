from http import HTTPStatus
from unittest import TestCase
from unittest.mock import patch

import app
from app.exceptions.exceptions import RoleNotFoundException, RoleScopesNotFoundException
from tests.responses.responses_views import *


class TestRoleScopeViews(TestCase):
    def setUp(self):
        self.app = app.create_app(start_orm=False).test_client()
        self.app.testing = True

    def test_ping(self):
        result = self.app.get("scopes/role/ping")
        self.assertEqual(PONG_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_id")
    def test_get_role_scopes_by_id_OK(self, role_scopes_mock):
        role_scopes_mock.return_value = SCOPES_OK_RESPONSE

        result = self.app.get(f"scopes/role/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_SCOPES_OK_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_id")
    def test_get_role_scopes_by_id_NOT_FOUND_role(self, role_scopes_mock):
        role_scopes_mock.side_effect = RoleNotFoundException(VALID_ROLE_ID)

        result = self.app.get(f"scopes/role/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_NOT_FOUND_ID_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_id")
    def test_get_role_scopes_by_id_NOT_FOUND_role_scopes(self, role_scopes_mock):
        role_scopes_mock.side_effect = RoleScopesNotFoundException(VALID_ROLE_NAME)

        result = self.app.get(f"scopes/role/{VALID_ROLE_ID}")
        self.assertEqual(ROLE_SCOPES_NOT_FOUND_NAME_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_name")
    def test_get_role_scopes_by_name_OK(self, role_scopes_mock):
        role_scopes_mock.return_value = SCOPES_OK_RESPONSE

        result = self.app.get(f"scopes/role/name/{VALID_ROLE_NAME}")
        self.assertEqual(ROLE_SCOPES_OK_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.OK, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_name")
    def test_get_role_scopes_by_name_NOT_FOUND_role(self, role_scopes_mock):
        role_scopes_mock.side_effect = RoleNotFoundException(VALID_ROLE_NAME)

        result = self.app.get(f"scopes/role/name/{VALID_ROLE_NAME}")
        self.assertEqual(ROLE_NOT_FOUND_NAME_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)

    @patch("app.role_scope_controller.get_role_scopes_by_name")
    def test_get_role_scopes_by_name_NOT_FOUND_role_scopes(self, role_scopes_mock):
        role_scopes_mock.side_effect = RoleScopesNotFoundException(VALID_ROLE_NAME)

        result = self.app.get(f"scopes/role/name/{VALID_ROLE_NAME}")
        self.assertEqual(ROLE_SCOPES_NOT_FOUND_NAME_RESPONSE, result.json)
        self.assertEqual(HTTPStatus.NOT_FOUND, result.status_code)
