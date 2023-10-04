from rest_framework.permissions import BasePermission

class StudyCenterPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff
      
class StudyCenterDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'PUT':
            return request.user.is_staff
        elif request.method == 'DELETE':
            return request.user.is_staff

        
class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff
    
class TeacherDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method == 'PUT':
            return request.user.is_staff
        elif request.method == 'DELETE':
            return request.user.is_staff

class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == ['GET', 'POST']:
            return request.user.is_staff
        
class StudentDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == ['GET', 'PUT', 'DELETE']:
            return request.user.is_staff
        