from django.urls import path
from . import views

urlpatterns = [
     path('', views.index),
     # path('get-all-posts', views.GetAllPosts),
     path('create-new-user', views.CreateUser),
     path('get-users', views.GetUsers),
     path('delete-user', views.DeleteUser),
     # path('get-post', views.GetPost),
     # path('update-post', views.UpdatePost),
     path('test-connection', views.TestConnection),
     path('detect-face', views.DetectFace),
     path('get-count-face-photo-byid', views.GetCountFacesPhotoById),
     path('training-model', views.TraningModel)
]