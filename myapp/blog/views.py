from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, UserSerializer
from .models import Category, Posts, Comment
from .permissions import UserPermission, PostsPermission, CommentPermission
from rest_framework.response import Response
from rest_framework import status

import json

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostsPermission,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=self.request.user)

            return Response(serializer.data,  status.HTTP_201_CREATED)

        return Response(dict(serializer.errors), status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (CommentPermission,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)

            return Response(serializer.data,  status.HTTP_201_CREATED)

        return Response(dict(serializer.errors), status.HTTP_400_BAD_REQUEST)
