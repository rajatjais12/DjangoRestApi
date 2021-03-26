from django.conf.urls import url 
from tutorials import views 
from django.urls import path
 

urlpatterns = [ 
    url(r'^api/song$', views.song_list),
    url(r'^api/song/(?P<pk>[0-9]+)$', views.song_d),
    url(r'^api/song/published$', views.song_published),
    url(r'^api/podcast$', views.podcast_list),
    url(r'^api/podcast/(?P<pk>[0-9]+)$', views.podcast_d),
    url(r'^api/podcast/published$', views.podcast_published),
    url(r'^api/audiobook$', views.audiobook_list),
    url(r'^api/audiobook/(?P<pk>[0-9]+)$', views.audiobook_d),
    url(r'^api/audiobook/published$', views.audiobook_published),
]