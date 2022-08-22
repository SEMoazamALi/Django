from rest_framework.routers import DefaultRouter
from .views import User_list, Post_list
from django.urls import path, include

router = DefaultRouter()
router2 = DefaultRouter()

router.register('user_list', User_list, basename='url_list')
router2.register('post_list', Post_list, basename='post_urls ')
urlpatterns= [
    path('api/', include(router.urls)),
    path('postapi/', include(router2.urls))
]