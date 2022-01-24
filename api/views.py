from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


@api_view(['GET'])
def last_tenant_contractor(request):
    queryset = TenantContractor.objects.last()
    serializer = TenantContractorSerializer(queryset)
    return Response(serializer.data)


@api_view(['GET'])
def last_brand(request):
    queryset = Brand.objects.last()
    serializer = BrandSerializer(queryset)
    return Response(serializer.data)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BrandCategoryTagViewSet(viewsets.ModelViewSet):
    queryset = BrandCategoryTag.objects.all()
    serializer_class = BrandCategoryTagSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class PremiseMainViewSet(viewsets.ModelViewSet):
    queryset = PremiseMain.objects.all()
    serializer_class = PremiseMainSerializer


class TenantContractorViewSet(viewsets.ModelViewSet):
    queryset = TenantContractor.objects.all()
    serializer_class = TenantContractorSerializer


class TenantContractorContactsViewSet(viewsets.ModelViewSet):
    queryset = TenantContractorContacts.objects.all()
    serializer_class = TenantContractorContactsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tenant_contractor_id']


class RentContractViewSet(viewsets.ModelViewSet):
    queryset = RentContract.objects.all()
    serializer_class = RentContractSerializer


class AdditionalAgreementViewSet(viewsets.ModelViewSet):
    queryset = AdditionalAgreement.objects.all()
    serializer_class = AdditionalAgreementSerializer


class RentContractPeriodicalFeeViewSet(viewsets.ModelViewSet):
    queryset = RentContractPeriodicalFee.objects.all()
    serializer_class = RentContractPeriodicalFeeSerializer


class RentContractOneTimeFeeViewSet(viewsets.ModelViewSet):
    queryset = RentContractOneTimeFee.objects.all()
    serializer_class = RentContractOneTimeFeeSerializer


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class RentContractUtilityFeeViewSet(viewsets.ModelViewSet):
    queryset = RentContractUtilityFee.objects.all()
    serializer_class = RentContractUtilityFeeSerializer


class RentContractSetupViewSet(viewsets.ModelViewSet):
    queryset = RentContractSetup.objects.all()
    serializer_class = RentContractSetupSerializer


class RentContractPeriodicalFeeSetupViewSet(viewsets.ModelViewSet):
    queryset = RentContractPeriodicalFeeSetup.objects.all()
    serializer_class = RentContractPeriodicalFeeSetupSerializer


class RentContractOneTimeFeeSetupViewSet(viewsets.ModelViewSet):
    queryset = RentContractOneTimeFeeSetup.objects.all()
    serializer_class = RentContractOneTimeFeeSetupSerializer


class RentContractUtilityFeeSetupViewSet(viewsets.ModelViewSet):
    queryset = RentContractUtilityFeeSetup.objects.all()
    serializer_class = RentContractUtilityFeeSetupSerializer


class BrandSearchFilter(ListAPIView):
    model = Brand
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    word_fields = ('brand_name',)
