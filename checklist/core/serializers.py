from rest_framework import serializers
from core.models import CheckList


# class CheckListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     is_deleted = serializers.BooleanField()
#     is_archived = serializers.BooleanField()
#     created_on = serializers.DateTimeField()
#     updated_on = serializers.DateTimeField()


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'
