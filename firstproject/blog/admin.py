from django.contrib import admin
from firstproject.blog.models import Blogpost, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)

admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Author, AuthorAdmin)