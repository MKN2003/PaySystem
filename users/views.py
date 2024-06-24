from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from users.models import UserModel, UserCardModel, TransferModel
from users.serializers import UserModelSerializer, UserCardModelSerializer, TransferModelSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.


@api_view()
def hell_world(request):
    return Response({'message': 'Hello world'})

class TestAPIView(APIView):

    def get(self, request):
        users = UserModel.objects.all()
        user_serializers = UserModelSerializer(users, many=True)
        return Response(user_serializers.data)

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelListAPIView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    permission_classes = [permissions.AllowAny]


class UserModelCreateAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserModelUpdateAPIView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        pass


class UserModelRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserModelDestroyAPIView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserCardModelListAPIview(generics.ListAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCardModelCreateAPIview(generics.CreateAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCardModelRetrieveAPIview(generics.RetrieveAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class UserCardModelUpdateAPIview(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCardModelSerializer

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        pass


class UserCardModelDestroyAPIview(generics.DestroyAPIView):
    queryset = UserCardModel.objects.all()
    serializer_class = UserCardModelSerializer


class TransferModelListAPIview(generics.ListAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelCreateAPIview(generics.CreateAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelDestroyAPIview(generics.DestroyAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelUpdateAPIview(generics.UpdateAPIView):
    queryset = TransferModel.objects.all()
    serializer_class = TransferModelSerializer


class TransferModelRetrieveAPIview(generics.RetrieveAPIView):
    queryset = TransferModel.objects.all()
    serializer_class =TransferModelSerializer

