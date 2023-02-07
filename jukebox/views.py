from rest_framework.response import Response
from jukebox.models import Music
from jukebox.serializers import MusicSerializer
from rest_framework.views import APIView


class MusicList(APIView):
    def get(self, request):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)


class MusicRandom(APIView):
    def get(self, request):
        music = Music.objects.all().order_by('?')
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)


class SearchMusicByName(APIView):
    def get(self, request, title):
        music = Music.objects.get(title=title)
        serializer = MusicSerializer(music)
        return Response(serializer.data)


class SearchMusicByDate(APIView):
    def get(self, request):
        music = Music.objects.all().order_by('?')
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)


class AddMusic(APIView):
    def post(self, request):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
