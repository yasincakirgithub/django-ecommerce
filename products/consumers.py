import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class BucketConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )


    def receive(self, text_data):
        
        json_text = json.loads(text_data)
        json_text["type"] = "add_product"
        
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            json_text
        )
    
    def add_product(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))