from rest_framework import generics, filters
# from rest_framework.pagination import PageNumberPagination
from .pagination import CustomPageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ToDoItem
from .serializers import ToDoItemSerializer
from django.utils.decorators import method_decorator
import django_filters

class ToDoItemListView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends= [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id','title', 'description', 'completed']
    search_fields = ['id','title', 'description', 'completed']
    ordering_fields = ['id','title', 'description', 'completed']


class ToDoItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List To Do Items With Pagination and Search Functionality using query parameters':'GET /items',
        'Create':'POST /items/',
        'Retrieve':'GET /items/<id>/',
        'Update':'PUT /items/<id>/',
        'Delete': 'DELETE /items/<id>/'

    }
    return Response(api_urls)