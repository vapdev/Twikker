import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import apps.conversation.routing as conversation_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twikker.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            conversation_routing.websocket_urlpatterns
        )
    )
})