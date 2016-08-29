from django.contrib.auth.models import User, Group
from rest_framework import serializers
from weather_data.models import Region, Weather, TYPECHOICE

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')

######################################
# class RegionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Region` instance, given the validated data.
#         """
#         return Region.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Region` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.title)
#         instance.save()
#         return instance
######################################


class WeatherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    region = serializers.CharField(required=False, allow_blank=True, max_length=100)
    value = serializers.CharField(required=False, allow_blank=True, max_length=100)
    type = serializers.ChoiceField(choices=TYPECHOICE, default='Tmin')
    month = serializers.CharField(required=False, allow_blank=True, max_length=100)
    year = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Weather` instance, given the validated data.
        """
        return Weather.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Weather` instance, given the validated data.
        """
        instance.region = validated_data.get('region', instance.title)
        instance.value = validated_data.get('value', instance.code)
        instance.type = validated_data.get('type', instance.language)
        instance.month = validated_data.get('month', instance.style)
        instance.year = validated_data.get('year', instance.style)
        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

##################################
##################################
##################################

# import weather_data.models
# from weather_data.models import Region, Weather, TYPECHOICE
# from rest_framework import serializers
#
#
# class RegionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Region
#         fields = ('id', 'name')
#
#
# class WeatherSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Weather
#         fields = ('id', 'region', 'type', 'year', 'month', 'value')


