from rest_framework import permissions
from .models import EventPermission

class IsEventOwnerOrEditorOrViewer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if obj.owner == user:
            return True  # Full access for owner

        try:
            perm = EventPermission.objects.get(event=obj, user=user)
            if request.method in permissions.SAFE_METHODS:
                return True  # Editors and viewers can read
            return perm.role == 'editor'  # Only editors can write
        except EventPermission.DoesNotExist:
            return False
