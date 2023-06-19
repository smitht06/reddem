from django.contrib import admin
from .models import Post, Comment, Reply

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at", "updated_at")

class ReplyAdmin(admin.ModelAdmin):
    list_display = ("comment", "user", "created_at", "updated_at")

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)

