from rest_framework import viewsets

from simple_crud import models, serializers


class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
