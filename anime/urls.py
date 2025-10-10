from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimeViewSet, anime_list, anime_detail

router = DefaultRouter()
router.register(r'animes', AnimeViewSet, basename='anime')

urlpatterns = [
    path('api/', include(router.urls)),  # API routes
    path('', anime_list, name='anime_list'),  # Web route for anime list
    path('<int:pk>/', anime_detail, name='anime_detail'),  # Detail view
]
