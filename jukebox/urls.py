from django.urls import path
from jukebox.views import music_list, music_create, get_music_by_name, get_music_by_data


urlpatterns = [
    path('', music_create),
    path('list/', music_list),
    path('<str:title>', get_music_by_name),
    path('<str:get_music_by_data>', get_music_by_data)
]
