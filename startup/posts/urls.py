from django.urls import path
from . import views

app_name='posts'

urlpatterns=[
    path('',views.PostList.as_view(),name="postlist" ),
    path('createpost/',views.CreatePost.as_view(), name="create"),
    path('deletepost/', views.DeletePost.as_view(), name="delete"),
    path('userposts/', views.UserPosts.as_view(), name="user"),
]