from django.urls import path
from django.urls.conf import include

from rest_framework import routers

from news import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = router.urls
