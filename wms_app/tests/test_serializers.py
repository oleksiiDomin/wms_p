from django.test import TestCase

from wms_app.models import Seller, Calcium
from wms_app.serializers import SellerSerializer

class SellerSerializerTest(TestCase):

    def setUp(self):
        seller1 = Seller.objects.create(name = 'test1', country = 'US1', city = 'San Francisco1')
        seller2 = Seller.objects.create(name = 'test2', country = 'US2', city = 'San Francisco2')
        self.serializer = SellerSerializer([seller1, seller2], many=True).data

    def test_ok_1(self):
        seller1 = Seller.objects.create(name='test1', country='US1', city='San Francisco1')
        seller2 = Seller.objects.create(name='test2', country='US2', city='San Francisco2')

        # calcium1 = Calcium.objects.create(lot='0001', weight_of_lot=14000, seller=seller1)
        # calcium2 = Calcium.objects.create(lot='0002', weight_of_lot=14000, seller=seller1)
        # calcium3 = Calcium.objects.create(lot='0003', weight_of_lot=14000, seller=seller2)
        # calcium4 = Calcium.objects.create(lot='0004', weight_of_lot=14000, seller=seller2)
        # calcium5 = Calcium.objects.create(lot='0005', weight_of_lot=14000, seller=seller2)

        serializer = SellerSerializer([seller1, seller2], many=True).data

        expected = [
             {'name': 'test1',
              'country': 'US1',
              'materials': [],
              'city': 'San Francisco1',
              'materials_count': 0
              },

             {'name': 'test2',
              'country': 'US2',
              'city': 'San Francisco2',
              'materials': [],
              'materials_count': 0
              }
        ]

        print(serializer)
        print(expected)

        self.assertEqual(serializer, expected)

