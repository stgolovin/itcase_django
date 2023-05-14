from rest_framework import generics, filters
from django.core.cache import cache
from rest_framework.filters import SearchFilter
from itcase_app.models import Good
from itcase_app.serializers import GoodSerializer, GoodDetailSerializer


class GoodView(generics.ListAPIView):
    if cache.has_key('key'):
        my_value = cache.get('key')
        queryset = my_value
    else:
        queryset = Good.objects.all()
        cache.set('key', queryset, timeout=60)

    serializer_class = GoodSerializer
    filter_backends = [filters.OrderingFilter, SearchFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name', 'description', 'base_price',]


class ProductDetail(generics.RetrieveAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodDetailSerializer
