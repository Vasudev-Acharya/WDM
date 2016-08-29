from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('weather_data.urls')),
]
#
#
# from django.conf.urls import url, include
# from rest_framework import routers
# import weather_data
# from weather_data import views
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

####################################################################################
####################################################################################
####################################################################################

# from django.conf.urls import url, include
# from rest_framework import routers
#
# import weather_data
# from weather_data import views
# from weather_data.views import RegionViewSet, WeatherViewSet
# #
# # router = routers.DefaultRouter()
# # router.register(r'region', views.RegionViewSet)
# # router.register(r'weather', views.WeatherViewSet)
# #
# # # Wire up our API using automatic URL routing.
# # # Additionally, we include login URLs for the browsable API.
# # urlpatterns = [
# #     url(r'^', include(router.urls)),
# #     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# # ]
#
# #
# # from django.contrib import admin
# # from django.conf.urls import url, include
# #
# # from rest_framework import routers
# # from rest_framework.urlpatterns import format_suffix_patterns
# #
# # from weather_data.views import RegionViewSet, WeatherViewSet
# # from rest_framework import renderers
# #
# # router = routers.DefaultRouter()
# # router.register(r'region', RegionViewSet)
# # router.register(r'weather', WeatherViewSet)
# #
# # urlpatterns = [
# #     url(r'^', include('weather_data.urls')),
# #     url(r'^admin/', admin.site.urls),
# # ]
# #
# # urlpatterns = format_suffix_patterns(urlpatterns)
#
# # router = routers.DefaultRouter()
# # router.register(r'region', RegionViewSet)
# # router.register(r'weather', WeatherViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     #url(r'^', include(router.urls)),
#     url(r'^', include('weather_data.urls')),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]