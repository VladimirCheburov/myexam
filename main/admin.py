from django.contrib import admin
from .models import vcexam

@admin.register(vcexam)
class vcexamAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_date', 'created_at', 'is_public')
    search_fields = ('name', 'users__email')
    list_filter = ('is_public', 'created_at', 'exam_date')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'
