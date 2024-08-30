from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'published_date', 'updated_date')
    list_filter = ('published_date', 'author_name')
    search_fields = ('title', 'content', 'author_name')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)