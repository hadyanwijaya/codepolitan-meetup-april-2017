from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'category_list', 'author', 'created_at')
	search_fields = ['title', 'body']
	date_hierarchy = 'created_at'

admin.site.register(Posts, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'user', 'body', 'created_at')
	search_fields = ['body', 'post']
	date_hierarchy = 'created_at'

admin.site.register(Comment, CommentAdmin)