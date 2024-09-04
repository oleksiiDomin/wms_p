from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from wms_app.serializers import *



class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all().annotate(
        annotated_materials=Count('materials'),
    ).prefetch_related('materials')
    serializer_class = SellerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['country']
    search_fields = ['name', 'city', 'country']
    ordering_fields = ['name ']



class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]




class CalciumViewSet(ModelViewSet):
    queryset = Calcium.objects.all()
    serializer_class = CalciumSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['lot']

    @action(detail=False, methods=['get'])
    def total_balance(self, request, *args, **kwargs):
        total_balance = Calcium.objects.aggregate(current_balance=Sum('current_balance'))['current_balance']
        return Response({'total_balance': total_balance})



class CalciumSiliconViewSet(ModelViewSet):
    queryset = CalciumSilicon.objects.all()
    serializer_class = CalciumSiliconSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['lot']

    @action(detail=False, methods=['get'])
    def total_balance(self, request, *args, **kwargs):
        total_balance = CalciumSilicon.objects.aggregate(current_balance=Sum('current_balance'))['current_balance']
        return Response({'total_balance': total_balance})



class CarbonViewSet(ModelViewSet):
    queryset = Carbon.objects.all()
    serializer_class = CarbonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['lot']

    @action(detail=False, methods=['get'])
    def total_balance(self, request, *args, **kwargs):
        total_balance = Carbon.objects.aggregate(current_balance=Sum('current_balance'))['current_balance']
        return Response({'total_balance': total_balance})


class MetalStripViewSet(ModelViewSet):
    queryset = MetalStrip.objects.all()
    serializer_class = MetalStripSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['lot']

    @action(detail=False, methods=['get'])
    def total_balance(self, request, *args, **kwargs):
        total_balance = MetalStrip.objects.aggregate(current_balance=Sum('current_balance'))['current_balance']
        return Response({'total_balance': total_balance})



class MetalShotViewSet(ModelViewSet):
    queryset = MetalShot.objects.all()
    serializer_class = MetalShotSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['lot']

    @action(detail=False, methods=['get'])
    def total_balance(self, request, *args, **kwargs):
        total_balance = MetalShot.objects.aggregate(current_balance=Sum('current_balance'))['current_balance']
        return Response({'total_balance': total_balance})



class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.prefetch_related('orders__coils').all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['country']
    search_fields = ['name', 'city', 'country']
    ordering_fields = ['name ']



class OrderFilter(FilterSet):
    customer = filters.CharFilter(field_name='customer__id', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['customer']

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.prefetch_related('coils').all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = OrderFilter



class CoilFilter(FilterSet):
    order = filters.CharFilter(field_name='order__id', lookup_expr='icontains')
    customer = filters.CharFilter(field_name='customer__id', lookup_expr='icontains')

    class Meta:
        model = Coil
        fields = ['order', 'customer']

class CoilViewSet(ModelViewSet):
    queryset = Coil.objects.all()
    serializer_class = CoilSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = CoilFilter



class IncludedMaterialFilter(FilterSet):
    order = filters.CharFilter(field_name='order__id', lookup_expr='icontains')

    class Meta:
        model = IncludedMaterial
        fields = ['order']

class IncludedMaterialViewSet(ModelViewSet):
    queryset = IncludedMaterial.objects.all()
    serializer_class = IncludedMaterialSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = IncludedMaterialFilter





