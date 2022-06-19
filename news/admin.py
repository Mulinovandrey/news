from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_puplished')
    list_display_links = ('id', 'title')
    search_fields = ('titile', 'content')

admin.site.register(News, NewsAdmin)
