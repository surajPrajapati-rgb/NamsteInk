from django.contrib import admin
from .models import Post, Author, Tag, Comment
# Register your models here.

# Register your models here.
# class BookAdmin(admin.ModelAdmin):
#     # readonly_fields=("slug",)
#     prepopulated_fields={"slug":("title",)}


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields={"slug":("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)