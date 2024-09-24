from django.db import models
from django.conf import settings

# Model for Lost and Found items
class LostFoundItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Owner of the post
    ITEM_TYPES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    item_name = models.CharField(max_length=255)
    description = models.TextField()
    date_lost_found = models.DateField()
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    item_type = models.CharField(max_length=5, choices=ITEM_TYPES)  # 'lost' or 'found'
    image = models.ImageField(upload_to='lost_found_images/', blank=True, null=True)  # Optional image
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item_name} ({self.item_type})'


# Model for potential matches between lost and found items
class PotentialMatch(models.Model):
    lost_item = models.ForeignKey(LostFoundItem, on_delete=models.CASCADE, related_name='lost_item')
    found_item = models.ForeignKey(LostFoundItem, on_delete=models.CASCADE, related_name='found_item')
    matched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Match between {self.lost_item.item_name} and {self.found_item.item_name}'


# Optional: In-App Messages between users regarding lost and found items
class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    item = models.ForeignKey(LostFoundItem, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username}'
