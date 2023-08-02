from . import views
from django.urls import path

urlpatterns = [
    path('', views.ApiOverview, name='api-overview'),
    # path('todolist/', ),
    # path('create/',views.create, name='create' ),
    # path('item/<int:pk>/', ),
    # path('item/<int:pk>/update/', ),
    # path('item/<int:pk>/delete/', ),

    # path('csvupload/'),
    # path('csvexport/'),
    path('items/',views.ToDoItemListView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', views.ToDoItemRetrieveUpdateDestroyView.as_view(), name='item-detail')

]