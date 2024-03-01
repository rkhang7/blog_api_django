from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     # path('get-all-posts', views.GetAllPosts),
     path('create-new-user', views.CreateUser),
     path('get-users', views.GetUsers),
     # path('delete-post', views.DeletePost),
     # path('get-post', views.GetPost),
     # path('update-post', views.UpdatePost),
     path('test-connection', views.TestConnection),
     path('detect-face', views.DetectFace),
]