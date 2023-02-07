from django.urls import path
from jukebox.views import MusicList, SearchMusicByName, AddMusic, MusicRandom, SearchMusicByDate


urlpatterns = [
    path('list/', MusicList.as_view()),
    path('list/random', MusicRandom.as_view()),
    path('list/<str:title>', SearchMusicByName.as_view()),
    path('list/<str:published_year>', SearchMusicByDate.as_view()),
    path('create/', AddMusic.as_view()),
]
