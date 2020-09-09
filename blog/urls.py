"""from django.urls import path

from blog.api import views as api_views

urlpatterns = [
    #path("", PostsListView.as_view()),
    path("api/posts/", api_views.PostListView.as_view(), name="api_post_list"),
    path("api/posts/<pk>", api_views.CommentDetailView.as_view(), name="api_post_detail"),
] """