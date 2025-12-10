from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Admin = can access all tasks
    User  = can access only own tasks
    """

    def has_object_permission(self, request, view, obj):
        # Admin allowed
        if request.user.is_staff:
            return True

        # User allowed only if owner
        return obj.owner == request.user
