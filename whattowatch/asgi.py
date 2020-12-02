import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import watch.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whattowatch.settings")

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            watch.routing.websocket_urlpatterns
        )
    ),
})
