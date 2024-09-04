from django.db.models import Sum

from wms_app.models import Coil


def set_sum_of_weight():
    return Coil.objects.all().aggregate(sum=Sum('weight')).get('sum')


