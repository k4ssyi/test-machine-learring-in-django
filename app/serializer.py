from rest_framework import serializers

from .models import Iris


class IrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iris
        fields = ('sepal_length', 'sepal_width',
                  'petal_length', 'petal_width', 'score')
