from rest_framework import viewsets
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


class TenantContractorViewSet(viewsets.ModelViewSet):
    queryset = TenantContractor.objects.all()
    serializer_class = TenantContractorSerializer


class RentContractViewSet(viewsets.ModelViewSet):
    queryset = RentContract.objects.all()
    serializer_class = RentContractSerializer
