from django.urls import path
from .views import *

urlpatterns = [
    path('transfer/', TransferModelListAPIview.as_view()),
    path('transfer/create', TransferModelCreateAPIview.as_view()),
    path('transfer/update<int:pk>', TransferModelUpdateAPIview.as_view()),
    path('transfer/delete<int:pk>', TransferModelDestroyAPIview.as_view()),
    path('transfer/update<int:pk>', TransferModelRetrieveAPIview.as_view()),
]