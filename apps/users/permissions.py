from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        message = "You haven't permission to do this dude."
        isOwner = request.user == obj.user
        if isOwner:
            return isOwner
        else:
            raise PermissionDenied(detail=message)
