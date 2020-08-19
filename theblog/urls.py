from django.contrib import admin
from django.urls import path

from  .views import HomeView,ArticleDetailsView,AddPostView,UpdatePostView,DeletePostView
urlpatterns = [
    
    # path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailsView.as_view(),name = 'articledetail'),
    path('addpost/',AddPostView.as_view(),name='addpost'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),
]