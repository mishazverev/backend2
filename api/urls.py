from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('categorytags', CategoryTagViewSet)
router.register('brands', BrandViewSet)
router.register('premises', PremiseMainViewSet)
router.register('tenants', TenantContractorViewSet)
router.register('rentcontracts', RentContractViewSet)


urlpatterns = [
    path('', include(router.urls))
]
