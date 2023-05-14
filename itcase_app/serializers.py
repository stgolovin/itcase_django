from rest_framework import serializers

from itcase_app.models import Good, Parameter, Image


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['name', 'value', 'price', 'sort_order',]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['file', 'caption', 'sort_order',]



class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'description', 'base_price', 'sort_order',]


class GoodDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    parameters = ParameterSerializer(read_only=True, many=True)

    class Meta:
        model = Good
        fields = ['id', 'name', 'description', 'base_price', 'sort_order', 'images', 'parameters', ]
