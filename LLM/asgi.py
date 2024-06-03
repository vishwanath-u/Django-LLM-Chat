import os

from channels.auth import AuthMiddlewareStack
from channels.router import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import langchain_stream.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LLM.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            langchain_stream.routing.websocket_urlpatterns
        )
    ),
})
