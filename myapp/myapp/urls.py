from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from blog import views as blog_views

router = routers.DefaultRouter()
router.register(r'users', blog_views.UserViewSet)
router.register(r'categories', blog_views.CategoryViewSet)
router.register(r'posts', blog_views.PostViewSet)
router.register(r'comments', blog_views.CommentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
	url(r'^api-token-auth/', views.obtain_auth_token)
]
