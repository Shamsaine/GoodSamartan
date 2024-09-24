from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .models import LostFoundItem, PotentialMatch, Message
from .serializers import LostFoundItemSerializer, PotentialMatchSerializer, MessageSerializer

# Filters for LostFoundItem
class LostFoundItemFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='posted_at', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='posted_at', lookup_expr='lte')
    item_type = filters.CharFilter(field_name='item_type')

    class Meta:
        model = LostFoundItem
        fields = ['location', 'start_date', 'end_date', 'item_type']


# View for listing and creating lost and found items
class LostFoundItemListCreateView(generics.ListCreateAPIView):
    queryset = LostFoundItem.objects.all().order_by('-posted_at')
    serializer_class = LostFoundItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LostFoundItemFilter
    search_fields = ['item_name', 'description']
    ordering_fields = ['posted_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# View for retrieving, updating, or deleting a specific lost or found item
class LostFoundItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LostFoundItem.objects.all()
    serializer_class = LostFoundItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only allow users to retrieve, update, or delete their own items
        return self.queryset.filter(user=self.request.user)


# View for retrieving recent lost and found items (e.g., last 5 items)
class RecentLostItemsView(generics.ListAPIView):
    queryset = LostFoundItem.objects.order_by('-posted_at')[:5]  # Fetch 5 most recent items
    serializer_class = LostFoundItemSerializer
    permission_classes = [IsAuthenticated]


# View for retrieving potential matches between lost and found items
class PotentialMatchListView(generics.ListAPIView):
    queryset = PotentialMatch.objects.all()
    serializer_class = PotentialMatchSerializer
    permission_classes = [IsAuthenticated]


# View for listing and sending messages between users
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('-sent_at')
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Save the sender as the current user
        serializer.save(sender=self.request.user)


# View for listing items posted by the logged-in user
class UserLostFoundItemsView(generics.ListAPIView):
    serializer_class = LostFoundItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only retrieve items posted by the currently authenticated user
        return LostFoundItem.objects.filter(user=self.request.user)
