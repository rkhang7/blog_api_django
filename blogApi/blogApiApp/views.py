from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .utils import Utils
from .faces_manager import FacesManager
import cv2

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was sccessful"})

# @api_view(['GET'])
# def GetAllPosts(request):
#     get_posts = Post.objects.all()
#     serializer = PostSerializer(get_posts, many = True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# def CreatePost(request):
#     data = request.data
#     serializer = PostSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"Success": "The post has successfully created"}, status=201)
#     else:
#         return Response(serializer.errors, status=400)
    

    
# @api_view(['GET'])
# def GetPost(request):
#     post_id = request.data.get('post_id')
#     try:
#         post = Post.objects.get(id=post_id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=200)
#     except Post.DoesNotExist:
#         return Response({"Error": "The post does not exist"}, status=404)
    
# @api_view(['PUT'])
# def UpdatePost(request): 
#     post_id = request.data.get('post_id')
#     get_new_title = request.data.get('new_title')
#     get_new_content = request.data.get('_new_content')
#     try:
#         post = Post.objects.get(id=post_id)

#         if get_new_title:
#             post.title = get_new_title
#         if get_new_content:
#             post.title = get_new_content
        
#         post.save()
#         return Response({"Success": "The post was successfully updated"}, status=200)
#     except Post.DoesNotExist:
#         return Response({"Error": "The post does not exist"}, status=404)

@api_view(['POST'])
def CreateUser(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True ,"message": "The user has successfully created"}, status=200)
    else:
        return Response({"success": False, "message": serializer.errors}, status=400)

@api_view(['GET'])
def GetUsers(request):
    get_users = User.objects.all()
    serializer = UserSerializer(get_users, many = True)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteUser(request):
    user_id = request.data.get('id')
    try:
        post = User.objects.get(id=user_id)
        post.delete()
        return Response({"success": True, "message": "The user was successfully deleted"}, status=200)
    except User.DoesNotExist:
        return Response({"message": "The user does not exist"}, status=404)

@api_view(['GET'])
def TestConnection(request):
    return Response({"messsage": "Connected"}, status=200)
    
# @api_view(['POST'])
# def DetectFace(request):
#     try:
#         base64_image = request.data.get('image')
#         image = Utils.SaveImage(base64_image)
#         id,dist = FacesManager.Recognizer(image)
#         return Response({"message": "The image was successfully uploaded", "dist": dist, "id": id}, status=200)
#     except Exception as e:
#         return Response({"message": e }, status=404)
    
@api_view(['POST'])
def DetectFace(request):
    user_id = request.data.get('userId')
    base64_image = request.data.get('image')
    try:
        image = Utils.ConvertBase64ToImage(base64_image)
        if FacesManager.Detect2(str(user_id), image) == True:
            return Response({"success": True, "message": "The image was successfully uploaded"}, status=200)
        else:
            return Response({"success": False ,"message": "Do not upload more than 10 photos"}, status=200)
    except Exception as e:
        return Response({"success": False  ,"message": e }, status=404)
    
@api_view(['GET'])
def GetCountFacesPhotoById(request):
    id = request.data.get('userId')
    try:
        sampleNum = Utils.CountFilesById('faces/', str(id))
        return Response({"success": True , "count": sampleNum}, status=200)
    except Exception as e:
        return Response({"success": False  ,"message": e }, status=404)
    
@api_view(['POST'])
def TraningModel(request):
    try:
        FacesManager.TrainingModel()
        return Response({"success": True , "message": "Success"}, status=200)
    except Exception as e:
        return Response({"success": False  ,"message": e }, status=404)
   





