from rest_framework.response import Response
from rest_framework.decorators import api_view
from jukebox.models import Music
from jukebox.serializers import MusicSerializer


@api_view(['GET'])
def music_list(request):
    music = Music.objects.all()
    serializer = MusicSerializer(music, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_music_by_name(request, title):
    music = Music.objects.get(title=title)
    serializer = MusicSerializer(music)
    return Response(serializer.data)


@api_view(['GET'])
def get_music_by_data(request, published_year):
    music = Music.objects.get(published_year=published_year)
    serializer = MusicSerializer(music)
    return Response(serializer.data)


@api_view(['POST'])
def music_create(request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
