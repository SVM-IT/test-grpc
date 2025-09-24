from rest_framework import serializers

from something.models import Something


class SomethingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Something
        fields = "__all__"
