from django.conf import settings
from django.conf.urls.defaults import *
from traffic_log.models import *
from django.views.generic import *

urlpatterns = patterns('',
                       (r'^/?$', 'traffic_log.views.index'),
                       (r'^spot/?$','traffic_log.views.listSpots'),
                       (r'^spot/create/?$', 'traffic_log.views.createSpot'),
                       (r'^spot/edit/(?P<spot_key>[^\.^/]+)$', 'traffic_log.views.editSpot'),
                       (r'^spot/delete/(?P<spot_key>[^\.^/]+)$', 'traffic_log.views.deleteSpot'),
                       (r'^spot/(?P<spot_key>[^\.^/]+)/?$', 'traffic_log.views.spotDetail'),
                       (r'^spot_constraint/?$', 'traffic_log.views.listSpotConstraints'),
                       (r'^spot_constraint/create/?$', 'traffic_log.views.createSpotConstraint'),
                       (r'^spot_constraint/delete/(?P<spot_constraint_key>[^\.^/]+)$', 'traffic_log.views.deleteSpotConstraint'),
                       (r'^add_spot_to_constraint/(?P<spot_constraint_key>[^\.^/]+)$', 'traffic_log.views.addSpotToConstraint'),
                       )