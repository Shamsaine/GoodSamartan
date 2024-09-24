from django.contrib import admin

# Register your models here.
from .models import LostFoundItem, PotentialMatch, Message

@admin.register(LostFoundItem)
class LostFoundItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type', 'user', 'date_lost_found', 'location')

@admin.register(PotentialMatch)
class PotentialMatchAdmin(admin.ModelAdmin):
    list_display = ('lost_item', 'found_item', 'matched_at')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'item', 'sent_at')