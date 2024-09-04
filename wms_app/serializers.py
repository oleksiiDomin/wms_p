from django.db.models import Count
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from wms_app.models import Seller, Customer, Coil, Calcium, CalciumSilicon, Carbon, Order, MetalStrip, MetalShot, \
    IncludedMaterial, Material


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'



class CalciumSerializer(ModelSerializer):
    class Meta:
        model = Calcium
        fields = '__all__'



class CalciumSiliconSerializer(ModelSerializer):
    class Meta:
        model = CalciumSilicon
        fields = '__all__'



class CarbonSerializer(ModelSerializer):
    class Meta:
        model = Carbon
        fields = '__all__'



class MetalStripSerializer(ModelSerializer):
    class Meta:
        model = MetalStrip
        fields = '__all__'



class MetalShotSerializer(ModelSerializer):
    class Meta:
        model = MetalShot
        fields = '__all__'



class CoilSerializer(ModelSerializer):
    class Meta:
        model = Coil
        fields = '__all__'



class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('lot', 'type', 'customer', 'created_at', 'quality_certificate', 'customer', 'coils')

    coils = CoilSerializer(many=True, read_only=True)



class IncludedMaterialSerializer(ModelSerializer):
    class Meta:
        model = IncludedMaterial
        fields = '__all__'



class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ('name', 'country', 'city', 'materials', 'materials_count', 'annotated_materials')

    materials = MaterialSerializer(many=True, read_only=True)
    materials_count = serializers.SerializerMethodField()
    annotated_materials = serializers.IntegerField()

    def get_materials_count(self, obj):
        return Material.objects.filter(seller = obj).count()



class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'country', 'city', 'orders', 'orders_count')

    orders = OrderSerializer(many=True, read_only=True)
    orders_count = serializers.SerializerMethodField()

    def get_orders_count(self, obj):
         return Order.objects.filter(customer = obj).count()