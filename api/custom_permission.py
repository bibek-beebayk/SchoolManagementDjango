from rest_framework.permissions import BasePermission
from rest_framework.response import Response

class RestrictDelete(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            else:
                return False

        return True
