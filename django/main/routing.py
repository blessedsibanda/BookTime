from django.urls import path
from channels.auth import AuthMiddlewareStack

from main import consumers
from booktime.auth import TokenGetAuthMiddlewareStack

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
    ),
    path(
        'mobile-api/my-orders/<int:order_id>/tracker/',
        TokenGetAuthMiddlewareStack(consumers.OrderTrackerConsumer),
    )
]