from rest_framework import generics, filters, status
# from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDoItem
from .serializers import ToDoItemSerializer, FileUploadSerializer
from django.utils.decorators import method_decorator
import django_filters
import pandas as pd

class ToDoItemListView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends= [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id','title', 'description', 'completed']
    search_fields = ['id','title', 'description', 'completed']
    ordering_fields = ['id','title', 'description', 'completed']
    ordering = 'id'


class ToDoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        
        for _,row in header.iterrows():
            new_file = File(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                completed=row['completed']
            )

            new_file.save()
        return Response({"status":"success"},status=status.HTTP_201_CREATED)


class ExportCsvView(APIView):
    def get(self,request):
        items = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(items,many=True)

        df = pd.DataFrame(serializer.data)
        df.to_csv(f"./export/excel/todoitems/data.csv", encoding="UTF-8", index=False)
        output={
            "status":status.HTTP_200_OK
        }
        return Response(output, status=status.HTTP_200_OK)


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List To Do Items With Pagination and Search Functionality using query parameters':'GET /items',
        'Create':'POST /items/',
        'Retrieve':'GET /items/<id>/',
        'Update':'PUT /items/<id>/',
        'Delete': 'DELETE /items/<id>/',
        'UploadCSV': 'PUT /uploadcsv/',
        'Export CSV':'GET /exportcsv/'


    }
    return Response(api_urls)