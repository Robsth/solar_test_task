from rest_framework.views import APIView
from rest_framework.response import Response

from .constants import STATUS_FILTER_OPTIONS
from .models import Site
from .serializers import SiteSerializer


class SiteList(APIView):
    """ Получаем список сайтов """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_queryset(self) -> queryset:
        """
        Фильтрует список сайтов по query params:
        ?status=available - показывает доступные сайты
        ?status=unavailable - показывает недоступные сайты
        """
        queryset = Site.objects.all()
        status = self.request.query_params.get('status')
        if status in STATUS_FILTER_OPTIONS.keys():
            queryset = queryset.filter(availability_status=STATUS_FILTER_OPTIONS[status])
        return queryset

    def get(self, request) -> Response:
        """
        Возвращает список сайтов.
        Для неавторизованных пользователей возвращает пустой список.
        """
        if request.user.is_authenticated:
            serializer = self.serializer_class(self.get_queryset(), many=True)
            return Response(serializer.data)
        else:
            return Response([])
