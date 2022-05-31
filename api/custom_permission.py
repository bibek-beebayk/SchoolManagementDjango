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


class RestrictUpdate(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH']:
            if request.user.is_superuser:
                return True
            else:
                return False
        return True

class ViewAssignmentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
    
        if request.user == obj.created_by:
            return True
        else:
            return False
