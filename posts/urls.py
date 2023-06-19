# urls for posts app

from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,  
    CommentUpdateView,
    CommentDeleteView,
    ReplyCreateView,
    ReplyUpdateView,
    ReplyDeleteView,
    UpvoteView,
    DownvoteView,
    CommentUpvoteView,
    CommentDownvoteView,
    ReplyUpvoteView,
    ReplyDownvoteView,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),
    path("<int:pk>/comment/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("<int:pk>/comment/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    path("<int:pk>/reply/", ReplyCreateView.as_view(), name="reply_create"),
    path("<int:pk>/reply/update/", ReplyUpdateView.as_view(), name="reply_update"),
    path("<int:pk>/reply/delete/", ReplyDeleteView.as_view(), name="reply_delete"),
    path("<int:pk>/upvote/", UpvoteView.as_view(), name="upvote"),
    path("<int:pk>/downvote/", DownvoteView.as_view(), name="downvote"),
    path("<int:pk>/comment/upvote/", CommentUpvoteView.as_view(), name="comment_upvote"),
    path("<int:pk>/comment/downvote/", CommentDownvoteView.as_view(), name="comment_downvote"),
    path("<int:pk>/reply/upvote/", ReplyUpvoteView.as_view(), name="reply_upvote"),
    path("<int:pk>/reply/downvote/", ReplyDownvoteView.as_view(), name="reply_downvote"),
]



