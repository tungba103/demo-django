from django.contrib.auth.models import Group, User, Permission
from django.contrib.admin.models import LogEntry
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'user_permissions' , 'get_user_permissions', 'get_group_permissions' ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename']
