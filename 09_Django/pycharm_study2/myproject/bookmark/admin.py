from django.contrib import admin
from bookmark.models import Bookmark

# admin을 조금 더 쉽게 이용하기 위한 register
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['name', 'url']
    list_filter = ['name', 'url']

# admin.site.register(Bookmark, BookmarkAdmin)