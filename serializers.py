from rest_framework import serializers

from simple_crud import models


class SerializerBase(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class UserSerializer(SerializerBase):
    class Meta:
        model = models.User
        fields = '__all__'
