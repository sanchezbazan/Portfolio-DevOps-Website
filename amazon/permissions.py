from rest_framework import permissions

class IsSuperuserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allows read-only access for any authenticated user
        return request.user and request.user.is_superuser  # Allows write access only for superusers
