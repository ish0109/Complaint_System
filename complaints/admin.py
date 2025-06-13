from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'date_filed')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description', 'user__username')
