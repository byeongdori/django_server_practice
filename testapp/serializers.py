from rest_framework import serializers
from . import models as testapp_model

class testApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = testapp_model.testApiModel
        fields = ('text',)