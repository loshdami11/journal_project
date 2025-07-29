from django.contrib import admin
from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'daily_prompt', 'gratitude_section', 'goals', 'date_created', 'is_done']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Journal, JournalAdmin)