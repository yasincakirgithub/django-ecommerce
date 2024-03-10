from django.urls import re_path
from . import consumers

products_websocket_urlpatterns = [
    re_path(r"ws/product/(?P<user_id>\w+)/bucket/", consumers.BucketConsumer.as_asgi()),
]