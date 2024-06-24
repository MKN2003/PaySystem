from django.urls import path
from .views import *

urlpatterns = [
    path('cards/', UserCardModelListAPIview.as_view()),
    path('cards/create<int:pk>', UserCardModelCreateAPIview.as_view()),
    path('cards/get<int:pk>', UserCardModelRetrieveAPIview.as_view()),
    path('cards/update<int:pk>', UserCardModelUpdateAPIview.as_view()),
    path('cards/delete<int:pk>', UserCardModelDestroyAPIview.as_view()),
]