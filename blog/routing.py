from django.urls import re_path
from blog import consumers

# Route the traffic to chat consumer
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer),
]
