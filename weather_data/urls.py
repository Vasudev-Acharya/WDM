from django.conf.urls import url
from weather_data import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^region/$', views.RegionList.as_view()),
    url(r'^region/(?P<pk>.*)/$', views.RegionDetail.as_view()),
    url(r'^RegionByName/(?P<loc_name>.*)/$', views.RegionByName),
    url(r'^weather/$', views.WeatherList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#
#
# from django.conf.urls import url, include
#
# from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers
#
# from weather_data import views
# from weather_data.views import RegionViewSet, api_root
# from rest_framework import renderers
#
# region_list = RegionViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# region_detail = RegionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# urlpatterns = format_suffix_patterns([
#     # url(r'^$', api_root),
#     url(r'^region/$', views.region_list),
#     url(r'^region/(?P<pk>[0-9]+)/$', region_detail, name='region-detail')
# ])
#
#
