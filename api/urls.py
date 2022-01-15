from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register('buildings', BuildingViewSet)

router.register('categorytags', CategoryTagViewSet)
router.register('brands', BrandViewSet)
router.register('premises', PremiseMainViewSet)
router.register('tenants', TenantContractorViewSet)
router.register('rentcontracts', RentContractViewSet)
router.register('additional-agreements', AdditionalAgreementViewSet)
router.register('rent-contract-periodical-fee', RentContractPeriodicalFeeViewSet)
router.register('rent-contract-one-time-fee', RentContractOneTimeFeeViewSet)
router.register('counters', CounterViewSet)
router.register('rent-contract-utility-fee', RentContractUtilityFeeViewSet)
router.register('rent-contract-setup', RentContractSetupViewSet)
router.register('rent-contract-periodical-fee-setup', RentContractPeriodicalFeeSetupViewSet)
router.register('rent-contract-one-time-fee-setup', RentContractOneTimeFeeSetupViewSet)
router.register('rent-contract-utility-fee-setup', RentContractUtilityFeeSetupViewSet)

router.register('tenantcontacts', TenantContractorContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lasttenant', views.last_tenant_contractor),
    path('lastbrand', views.last_brand)

]
