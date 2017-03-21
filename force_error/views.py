from django.core.exceptions import PermissionDenied


class ForcedError(Exception):
    pass


def force_error_view(request):
    raise ForcedError("Visited force_error")


def force_permission_denied_view(request):
    raise PermissionDenied("Visited force_permission_denied")
