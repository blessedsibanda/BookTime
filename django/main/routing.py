from django.urls import path
from channels.auth import AuthMiddlewareStack

from main import consumers

websocket_urlpatterns = [
    path(
        'ws/customer-service/<int:order_id>/',
        consumers.ChatConsumer
    ),
]

http_urlpatterns = [
    path(
        'customer-service/notify/',
        AuthMiddlewareStack(
            consumers.ChatNotifyConsumer
        )
    )
]