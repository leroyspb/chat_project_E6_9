from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('chats', ChatViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
