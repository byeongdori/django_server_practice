from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register('testapp', views.testApiViewSet)

urlpatterns = [
    url(r'^testview/', views.testView),
    url(r'^', include(router.urls)),
]