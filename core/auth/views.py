from django.contrib.auth.models import Group, User, Permission
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .serializers import GroupSerializer, UserSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all().order_by('id').reverse()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
