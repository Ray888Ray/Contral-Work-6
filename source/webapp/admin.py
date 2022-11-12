from django.contrib import admin
from webapp.models import BookGuest

# Register your models here.


class BookGuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'content', 'create', 'update', 'choice']
    list_display_links = ['name']
    list_filter = ['content']
    search_fields = ['name', 'content']
    exclude = []
    readonly_fields = ['create', 'update']


admin.site.register(BookGuest, BookGuestAdmin)
