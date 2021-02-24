from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import Plumber, Clients
from users.serializers import UserClientSerializer, UserPlumberSerializer


class ClientViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Clients.objects.all()
    serializer_class = UserClientSerializer


class PlumberViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Plumber.objects.all()
    serializer_class = UserPlumberSerializer

    # def get_permissions(self):
    #     if self.action == 'retrieve' or self.action == 'partial_update':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]
