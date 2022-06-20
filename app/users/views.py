from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import User
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class UserView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def create(self,request):
        res = request.data
        item = User.objects.filter(email=res.get('email')).count()
        if(item!=0):
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            item = UserSerializer(data=res)
            item.is_valid(raise_exception=True)
            item.save()
            return Response(status=status.HTTP_201_CREATED)


class Login(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            items = User.objects.filter(email=res.get('email'),password=res.get('password')).count()
            if(items>0):
               items = User.objects.filter(email=res.get('email'),password=res.get('password')) 
               items = UserSerializer(items,many=True)
               print(items.data)
               return Response(status=status.HTTP_200_OK,data=items.data)
            return Response(status=status.HTTP_200_OK,data="no_data")
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])




