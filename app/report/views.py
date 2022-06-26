from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Report
from .serializers import ReportSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class ReportView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

    def list(self,request):
        items = Report.objects.filter(is_respo='no')
        serializers =  ReportSerializer(items,many=True)
        listitem=[]
        for x in serializers.data:
            listitem.append({"date":x['date'],"id":x['id'],"email":x['email'],"user_id":x['user_id'],"account_type":'Client',"category":x['category'],"title":x['title'],"message":x['message'],"is_viewed":x['is_viewed'],"is_replied":x['is_replied'],"updated_by":x['updated_by']})
        print('okay')
        
        return Response(status=status.HTTP_200_OK,data=listitem)


class ReportList(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Report.objects.filter(user_id=user_id,is_respo='no')
            serializers = ReportSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class ReportRespo(generics.GenericAPIView):
    def get(self,request,format=None,report_id=None):
        try:
            items = Report.objects.filter(report_id=report_id,is_respo='yes')
            serializers = ReportSerializer(items,many=True)
            print(serializers.data)
            return Response(status=status.HTTP_200_OK,data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])