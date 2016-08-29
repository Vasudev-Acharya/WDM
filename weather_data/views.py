from weather_data.serializers import UserSerializer, GroupSerializer, RegionSerializer, WeatherSerializer
from weather_data.models import Region, Weather
from rest_framework import generics

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

@api_view(['GET'])
def RegionByName(request, loc_name):
    try:
        region = Region.objects.get(name=loc_name)
    except Region.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    serializer = RegionSerializer(region)
    return Response(serializer.data)

class WeatherList(generics.ListCreateAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer