from rest_framework import permissions

class UserPermission (permissions.BasePermission):

	def has_permission(self, request, view):
		if view.action in ['list', 'retrieve']:
			return True
		elif view.action in ['update', 'partial_update']:
			return request.user.is_authenticated() or request.user.is_staff
		elif view.action in ['create', 'destroy']:
			return request.user.is_staff
		else:
			return False

	def has_object_permission(self, request, view, obj):
		if view.action in ['retrieve']:
		    return True
		elif view.action in ['update', 'partial_update']:
		    return (obj == request.user or request.user.is_staff)
		elif view.action in ['destroy']:
			return request.user.is_staff
		else:
		    return False

class PostsPermission (permissions.BasePermission):

	def has_permission(self, request, view):
		if view.action in ['list', 'retrieve']:
			return True
		elif view.action in ['create', 'destroy', 'update', 'partial_update']:
			return request.user.is_authenticated() or request.user.is_staff
		else:
			return False

	def has_object_permission(self, request, view, obj):
		if view.action in ['retrieve']:
		    return True
		elif view.action in ['update', 'partial_update', 'destroy']:
		    return (obj.author == request.user or request.user.is_staff)
		else:
		    return False

class CommentPermission (permissions.BasePermission):

	def has_permission(self, request, view):
		if view.action in ['list', 'retrieve']:
			return True
		elif view.action in ['create', 'destroy', 'update', 'partial_update']:
			return request.user.is_authenticated() or request.user.is_staff
		else:
			return False

	def has_object_permission(self, request, view, obj):
		if view.action in ['retrieve']:
		    return True
		elif view.action in ['update', 'partial_update', 'destroy']:
		    return (obj.user == request.user or request.user.is_staff)
		else:
		    return False
