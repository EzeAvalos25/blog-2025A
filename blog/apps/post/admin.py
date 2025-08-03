from django.contrib import admin
from apps.post.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','author', 'category', 'created_at', 'update_at', 'allow_comments')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('category', 'author', 'created_at', 'allow_comments')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
