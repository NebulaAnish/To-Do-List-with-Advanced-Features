from . import views
from django.urls import path

urlpatterns = [
    path('', views.ApiOverview, name='api-overview'),
    path('items/',views.ToDoItemListView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', views.ToDoItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),

    path('uploadcsv/',views.CSVFileUploadView.as_view(),name='upload-csv'),
    path('exportcsv/', views.ExportCsvView.as_view(), name='export-csv'),
]