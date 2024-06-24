from rest_framework import serializers

from users.models import UserModel, UserCardModel, TransferModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserCardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCardModel
        fields = '__all__'


class TransferModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferModel
        fields = '__all__'

