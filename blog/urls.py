from django.urls import path
from blog.views import (createUser,About_View,PostDetailView,add_comment_to_post,post_publish,
                        PostListView,PostDetailView,CreatePostView,comment_approve,
                        UpdatePostView,DeletePostView,DraftListView,comment_remove)


app_name = 'blog'

urlpatterns = [
    path('signup/',createUser,name='signup'),
    path('',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('about/',About_View.as_view(),name='about'),
    path('post/new',CreatePostView.as_view(),name='post_view'),
    path('post/<int:pk>/edit',UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',DeletePostView.as_view(),name='post_delete'),
    path('drafts/',DraftListView.as_view(),name='drafts_list'),
    path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post'),
    path('comments/<int:pk>/approve',comment_approve,name='comment_approve'),
    path('comments/<int:pk>/delete',comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish',post_publish,name='post_publish'),
]
