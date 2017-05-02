from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Category (models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Posts (models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey(User)
	category = models.ManyToManyField(Category)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):

		return self.title + " - " + self.author.username

	def category_list(self):
	    return ', '.join([a.name for a in self.category.all()])

class Comment (models.Model):
	post = models.ForeignKey(Posts)
	user = models.ForeignKey(User)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):

		return self.user.username + " - " + self.body + " on " + self.post.body

