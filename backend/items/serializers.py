from rest_framework import serializers
from .models import LostFoundItem, PotentialMatch, Message


# Serializer for Lost and Found items
class LostFoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostFoundItem
        fields = [
            'id', 'user', 'item_name', 'description', 'date_lost_found',
            'location', 'contact_info', 'item_type', 'image', 'posted_at'
        ]
        read_only_fields = ['id', 'user', 'posted_at']


# Serializer for potential matches between lost and found items
class PotentialMatchSerializer(serializers.ModelSerializer):
    lost_item = LostFoundItemSerializer()  # Nested serializer for lost item details
    found_item = LostFoundItemSerializer()  # Nested serializer for found item details

    class Meta:
        model = PotentialMatch
        fields = ['id', 'lost_item', 'found_item', 'matched_at']
        read_only_fields = ['id', 'matched_at']


# Serializer for messages between users
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    item = LostFoundItemSerializer()  # Include item details in the message

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'item', 'message', 'sent_at']
        read_only_fields = ['id', 'sent_at']
