from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Posts, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'is_superuser')
        read_only_fields = ("is_superuser",)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name']

class PostSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Posts

		fields = ["url", "id", 'title', 'body', 'author', 'category', 'created_at']
		read_only_fields = ('author',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comment
		fields = ['url', 'id', 'post', 'body', 'user', 'created_at']
		read_only_fields = ("user",)