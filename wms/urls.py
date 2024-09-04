from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from rest_framework.routers import SimpleRouter

from wms_app import views

"""
URL configuration for wms project.

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
   1. Add an import:  from my_app import views
   2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
   1. Add an import:  from other_app.views import Home
   2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
   1. Import the include() function: from django.urls import include, path
   2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()

router = SimpleRouter()

router.register(r'material', views.MaterialViewSet)
router.register(r'seller', views.SellerViewSet)
router.register(r'calcium', views.CalciumViewSet)
router.register(r'calcium_silicon', views.CalciumSiliconViewSet)
router.register(r'carbon', views.CarbonViewSet)
router.register(r'metal_strip', views.MetalStripViewSet)
router.register(r'metal_shot', views.MetalShotViewSet)

router.register(r'customer', views.CustomerViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'coil', views.CoilViewSet)

router.register(r'included_material', views.IncludedMaterialViewSet)

urlpatterns += router.urls
#
# if not settings.TESTING:
#     urlpatterns = [
#         *urlpatterns,
#     ] + debug_toolbar_urls()

