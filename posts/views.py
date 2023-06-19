from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post, Comment, Reply

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 10


class PostDetailView(ListView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.kwargs["pk"])
        return context
    
class CommentDetailView(ListView):
    model = Comment
    template_name = "posts/comment_detail.html"
    context_object_name = "comment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["replies"] = Reply.objects.filter(comment=self.kwargs["pk"])
        return context
    

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class CommentCreateView(CreateView):
    model = Comment
    template_name = "posts/comment_create.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class ReplyCreateView(CreateView):
    model = Reply
    template_name = "posts/reply_create.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class PostUpdateView(CreateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CommentUpdateView(CreateView):
    model = Comment
    template_name = "posts/comment_update.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class ReplyUpdateView(CreateView):
    model = Reply
    template_name = "posts/reply_update.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class PostDeleteView(CreateView):
    model = Post
    template_name = "posts/post_delete.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CommentDeleteView(CreateView):
    model = Comment
    template_name = "posts/comment_delete.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class ReplyDeleteView(CreateView):
    model = Reply
    template_name = "posts/reply_delete.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    

class UpvoteView(CreateView):
    model = Post
    template_name = "posts/post_upvote.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DownvoteView(CreateView):
    model = Post
    template_name = "posts/post_downvote.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CommentUpvoteView(CreateView):
    model = Comment
    template_name = "posts/comment_upvote.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class CommentDownvoteView(CreateView):
    model = Comment
    template_name = "posts/comment_downvote.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class ReplyUpvoteView(CreateView):
    model = Reply
    template_name = "posts/reply_upvote.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
class ReplyDownvoteView(CreateView):
    model = Reply
    template_name = "posts/reply_downvote.html"
    fields = ["message"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.comment = Comment.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

