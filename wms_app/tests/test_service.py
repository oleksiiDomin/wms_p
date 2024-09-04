from django.test import TestCase

from wms_app.cache_service import set_sum_of_weight
from wms_app.models import Coil, Customer


class TestService(TestCase):
    def setUp(self):
        customer1 = Customer.objects.create(name='Customer 1', country='Country 1', city='City 1')
        customer2 = Customer.objects.create(name='Customer 2', country='Country 2', city='City 2')
        customer3 = Customer.objects.create(name='Customer 3', country='Country 3', city='City 3')

        coil1 = Coil.objects.create(number='0001', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer1)
        coil2 = Coil.objects.create(number='0002', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer1)
        coil3 = Coil.objects.create(number='0003', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer1)
        coil4 = Coil.objects.create(number='0004', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer2)
        coil5 = Coil.objects.create(number='0005', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer2)
        coil6 = Coil.objects.create(number='0006', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer3)
        coil7 = Coil.objects.create(number='0007', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer3)
        coil8 = Coil.objects.create(number='0008', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer3)
        coil9 = Coil.objects.create(number='0009', type='CK-30', length=4000, filling=215, metal_shel=200, weight=1500, customer=customer3)

    def test_ok(self):
        sum = 1500 * 9
        result = set_sum_of_weight()
        print(sum)
        print(result)
        self.assertEqual(sum, result)

    # def test_set_sum_of_weight(self):
        # serializer = CoilSerializer([self.coil1, self.coil2, self.coil3, self.coil3, self.coil4, self.coil5, self.coil6, coil7, coil8, coil9], many=True).data

        # print(set_sum_of_weight())
