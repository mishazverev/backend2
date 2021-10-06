from django_filters.rest_framework import DjangoFilterBackend
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


class CategoryTagViewSet(viewsets.ModelViewSet):
    queryset = CategoryTag.objects.all()
    serializer_class = CategoryTagSerializer


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
