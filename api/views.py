from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *


class CategoryTagViewSet(viewsets.ModelViewSet):
    queryset = CategoryTag.objects.all()
    serializer_class = CategoryTagSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class PremiseMainViewSet(viewsets.ModelViewSet):
    queryset = PremiseMain.objects.all()
    serializer_class = PremiseMainSerializer

    # def retrieve(self):
    #     queryset = PremiseMain.objects.last()
    #     serializer = PremiseMainSerializer(queryset)
    #     return Response(serializer.data)


class TenantContractorViewSet(viewsets.ModelViewSet):
    queryset = TenantContractor.objects.all()
    serializer_class = TenantContractorSerializer


class TenantContractorContactsViewSet(viewsets.ModelViewSet):
    queryset = TenantContractorContacts.objects.all()
    serializer_class = TenantContractorContactsSerializer


class RentContractViewSet(viewsets.ModelViewSet):
    queryset = RentContract.objects.all()
    serializer_class = RentContractSerializer
