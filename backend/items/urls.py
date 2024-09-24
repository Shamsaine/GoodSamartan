from django.urls import path
from .views import (
    LostFoundItemListCreateView,
    LostFoundItemDetailView,
    PotentialMatchListView,
    MessageListCreateView,
    UserLostFoundItemsView,
    RecentLostItemsView  # From the second set, fetches recent lost items
)

urlpatterns = [
    # List all lost/found items and create new ones
    path('lost-items/', LostFoundItemListCreateView.as_view(), name='lost-found-item-list-create'),
    
    # Detail, update, or delete a specific lost/found item
    path('lost-items/<int:pk>/', LostFoundItemDetailView.as_view(), name='lost-found-item-detail'),

    # View recent lost items (e.g., the 5 most recent)
    path('recent-lost-items/', RecentLostItemsView.as_view(), name='recent-lost-items'),

    # View items posted by the currently authenticated user
    path('user-lost-items/', UserLostFoundItemsView.as_view(), name='user-lost-items'),

    # View potential matches between lost and found items
    path('potential-matches/', PotentialMatchListView.as_view(), name='potential-match-list'),

    # List and create messages between users
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
]
