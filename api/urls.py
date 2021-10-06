from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register('categorytags', CategoryTagViewSet)
router.register('brands', BrandViewSet)
router.register('premises', PremiseMainViewSet)
router.register('tenants', TenantContractorViewSet)
router.register('rentcontracts', RentContractViewSet)
router.register('tenantcontacts', TenantContractorContactsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('lasttenant', views.last_tenant_contractor),
    path('lastbrand', views.last_brand)

]
