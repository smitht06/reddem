from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField("accounts.CustomUser", related_name="upvotes", blank=True)
    downvotes = models.ManyToManyField(
        "accounts.CustomUser", related_name="downvotes", blank=True
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(
        "accounts.CustomUser", related_name="comment_upvotes", blank=True
    )
    downvotes = models.ManyToManyField(
        "accounts.CustomUser", related_name="comment_downvotes", blank=True
    )

    def __str__(self):
        return self.message
    

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(
        "accounts.CustomUser", related_name="reply_upvotes", blank=True
    )
    downvotes = models.ManyToManyField(
        "accounts.CustomUser", related_name="reply_downvotes", blank=True
    )

    def __str__(self):
        return self.message
