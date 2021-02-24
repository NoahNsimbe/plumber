from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Clients, Plumber


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = '__all__'


class PlumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plumber
        fields = '__all__'


class UserClientSerializer(serializers.HyperlinkedModelSerializer):
    client = ClientSerializer(required=False)

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email', 'client',)

    def create(self, validated_data):
        client_data = validated_data.pop('client', {})

        created_user = User.objects.create(**validated_data)

        Clients.objects.create(user=created_user, **client_data)

        return created_user


class UserPlumberSerializer(serializers.HyperlinkedModelSerializer):
    plumber = PlumberSerializer(required=False)

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email', 'plumber',)
