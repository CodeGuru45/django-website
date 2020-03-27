from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<int:pk>', views.delete, name='post-delete'),
    path('user/<str:username>', views.user_posts, name='posts-user'),
    path('post/new/', views.create, name='post-create'),
]  