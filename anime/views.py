from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Anime
from .serializers import AnimeSerializer

# Django Template Views
def anime_list(request):
    query = request.GET.get('q')
    if query:
        animes = Anime.objects.filter(title__icontains=query)
    else:
        animes = Anime.objects.all().order_by('-rating')[:100]
    return render(request, 'anime/anime_list.html', {'animes': animes})

def anime_detail(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    return render(request, 'anime/anime_detail.html', {'anime': anime})


# Django REST Framework API View
class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.AllowAny]
