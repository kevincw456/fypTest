from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('main', views.analysisView)
urlpatterns = [
    path("analysis/", views.tweetsAnalysis),
    path("api/", include(router.urls)),
    path("home/", views.home, name = 'home'),
    path("form/", views.postRequest, name = 'tweetForm'),
    path("table/", views.table, name="table"),
    path("tweetRetrieval/", views.tweetRetrieval, name="tweetRetrieval"),
    path("twitterUserRetrieval/", views.twitterUserRetrieval, name="twitterUserRetrieval"),
]