from urllib import request
from rest_framework.permissions import SAFE_METHODS, BasePermission 
from django.contrib.auth.models import AnonymousUser

from account.models import User

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user, AnonymousUser):
            if request.user is User.Roles.STUDENT:
                return True
        return False



class IsSponsor(BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user,AnonymousUser):
            if request.user.role == User.Roles.SPONSOR:
                return True
        return False