from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Post
from .serializers import AuthenticateUserSerializer
from .serializers import UnAuthenticateUserSerializer
from .serializers import PostSerializer
from rest_framework import viewsets
from .permissions import ApiPermission, UserPermission

# class UserList(APIView):
    
#     def get(self, request):

#         if permissions.IsAuthenticated:

#             user = Account.objects.filter(pk = request.user.pk)
#             ser = UserSerializer(user, many = True)
#             return Response(ser.data)
#         else:

#             return HttpResponse("<h1>you are not authorized user</h1>")
            

#     # def post(self, request):
#     #     ser = UserSerializer(data=request.data)

#     #     ser.is_valid(raise_exception=True)

#     #     return Response(ser.data)
    



class User_list(viewsets.ViewSet):

    permission_classes = [UserPermission]

    def list(self, request):
        queryset = Account.objects.all()
        if request.user.is_authenticated:
            serializer_class = AuthenticateUserSerializer(queryset, many = True)
            return Response(serializer_class.data)
        else:
            serializer_class = UnAuthenticateUserSerializer(queryset, many = True)
            return Response(serializer_class.data)

    def create(self, request):
        # queryset = Account.objects.all()
        serializer_class = AuthenticateUserSerializer(data = request.data)
        return Response(serializer_class.data)

    def retrieve(self, request, pk):
        # pk = request.user.pk
        queryset = Account.objects.get(id = pk)
        if request.user.is_authenticated:
            serializer_class = AuthenticateUserSerializer(queryset)
            return Response(serializer_class.data)
        else:
            serializer_class = UnAuthenticateUserSerializer(queryset)
            return Response(serializer_class.data)
    
    def update(self, request, pk):
        
        queryset = Account.objects.get(id = pk)
        serializer_class = AuthenticateUserSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer_class.data)

    def destroy(self, request, pk):
        # pk = request.user.pk
        permission_classes = [UserPermission]
        if request.user.id == pk:
            query = Account.objects.get(id = pk)
            query.delete()
            return Response({'msg': 'Data Deleted'})
        else:
            return Response({'msg': "you're not authorized for this"})

    


class Post_list(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [ApiPermission]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


