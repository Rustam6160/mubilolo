from django.contrib import admin
from .models import Gift

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_whom', 'created_at')
    search_fields = ('title', 'for_whom')
