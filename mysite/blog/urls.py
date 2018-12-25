from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import (CreatePost,UserPostListView,PostEdit,PostDelete)

urlpatterns = [
    path('',views.postlist,name='post-list'),
    path('post/<int:id>/<str:slug>/',views.Post_detail,name='post-detail'),
    path('post/new/',views.CreatePost.as_view(),name='post-new'),
    path('user/<str:username>/',views.UserPostListView.as_view(),name='user-posts'),
    path('post/<int:id>/<str:slug>/edit/',views.PostEdit.as_view(),name='post-edit'),
    path('post/<int:id>/<str:slug>/delete/',views.PostDelete.as_view(),name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
