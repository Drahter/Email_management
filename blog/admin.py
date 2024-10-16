from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'views_counter',)
    search_fields = ('title', 'content',)
