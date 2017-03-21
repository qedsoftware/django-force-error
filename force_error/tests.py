from django.core.exceptions import PermissionDenied
from django.test import RequestFactory
from django.test import TestCase

from force_error.views import ForcedError, force_error_view, \
    force_permission_denied_view


class TestForceError(TestCase):
    def setUp(self):
        self.request = RequestFactory()

    def test_error(self):
        with self.assertRaises(ForcedError):
            force_error_view(self.request)

    def test_permission_denied(self):
        with self.assertRaises(PermissionDenied):
            force_permission_denied_view(self.request)
