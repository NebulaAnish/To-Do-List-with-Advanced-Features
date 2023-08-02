import django_filters
import pandas as pd
import csv

from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .pagination import CustomPageNumberPagination
from .models import ToDoItem
from .serializers import ToDoItemSerializer, CSVFileUploadSerializer

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


class CSVFileUploadView(generics.CreateAPIView):
    serializer_class = CSVFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        csv_file = request.data['csv_file']

        df = pd.read_csv(csv_file)
        items_to_create = df.to_dict(orient='records')

        ToDoItem.objects.bulk_create([ToDoItem(**item) for item in items_to_create])

        return Response({'message': 'CSV data Saved to the database.'}, status=status.HTTP_201_CREATED)

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
        'List with query parameters support':'GET /items',
        'Create':'POST /items/',
        'Retrieve':'GET /items/<id>/',
        'Update':'PUT /items/<id>/',
        'Delete': 'DELETE /items/<id>/',
        'UploadCSV': 'PUT /uploadcsv/',
        'Export CSV':'GET /exportcsv/'
    }
    return Response(api_urls)