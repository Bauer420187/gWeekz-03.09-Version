from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path("upload/", views.upload, name = "upload"),
    path("games/",views.games, name = "games"),
    path("profile/",views.profile, name = "profile"),
    path("index/",views.index,name = "index"),
    path("videos/",views.videos,name = "videos"),
    url(r'^$', views.all_rooms, name="all_rooms"),
    url(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
   
]