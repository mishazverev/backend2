from rest_framework import serializers
from .models import *


class CategoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTag
        fields = ('id', 'category_tag_name', 'category_tag_description')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name', 'brand_description', 'brand_category_tag')


class PremiseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiseType
        fields = ('id', 'type_name', 'type_description')


class PremiseMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiseMain
        fields = (
            'id',
            'number',

            'floor',
            'measured_area',
            'measurement_date',
            'contracted',
            'description',

            'ceiling_height',
            'facade_length',
            'fitout_condition',
            'electric_capacity',
            'cooling_capacity',
            'water_supply',
            'last_updated',
            'user_updated'
        )


class TenantContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantContractor
        fields = ('id',
                  'company_name',
                  'needed_premise_type',
                  'brands',

                  'contact_person_name',
                  'contact_person_position',
                  'contact_person_email',
                  'contact_person_phone',
                  'contact_person_mobile1',
                  'contact_person_mobile2',
                  'description',

                  'retail_premise_type',
                  'needed_min_area',
                  'needed_max_area',
                  'needed_ceiling_height',
                  'needed_facade_length',
                  'needed_fitout_condition',
                  'needed_electric_capacity',
                  'needed_cooling_capacity',
                  'needed_water_supply',
                  'needed_additional_requirements',

                  'legal_name',
                  'tax_id',
                  'signing_person_name',
                  'signing_person_position',
                  'legal_address',
                  'postal_address',

                  'kpp',
                  'bik',
                  'bank_name',
                  'current_account',
                  'correspondent_account',
                  'ogrn',
                  'okpo',
                  'registration_authority',
                  'legal_entity_certificate_number',

                  'last_updated',
                  'user_updated',
                  )


class RentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContract
        fields = (
            'id', 'premise_id', 'tenant_contractor_id', 'rent_contract_number', 'contracted_area', 'brand',
            'contract_signing_date', 'rent_start_date', 'stop_billing_date', 'premise_return_date',
            'duration_years', 'duration_months', 'duration_days', 'rent_fee_per_sqm', 'service_fee_per_sqm',
            'marketing_fee_per_sqm', 'turnover_fee', 'CA_utilities_compensation_fee_fixed',
            'utilities_compensation_type', 'CA_utilities_compensation_type',
            'rent_fee_indexation_type', 'service_fee_indexation_type', 'marketing_fee_indexation_type',
            'utilities_compensation_fixed_indexation_type', 'CA_utilities_compensation_fixed_indexation_type',
            'rent_fee_indexation_fixed', 'service_fee_indexation_fixed', 'marketing_fee_indexation_fixed',
            'utilities_compensation_fixed_indexation_fixed',
            'CA_utilities_compensation_fee_fixed_indexation_type_fixed',
            'act_of_transfer_signed', 'act_of_transfer_date', 'rent_fee_advance_payment_day',
            'service_fee_advance_payment_day', 'marketing_fee_advance_payment_day',
            'CA_utilities_compensation_fee_fixed_payment_day',
            'utilities_compensation_fixed_payment_day', 'guarantee_deposit_type',
            'guarantee_deposit_amount', 'guarantee_deposit_number_of_months',
            'guarantee_deposit_provided', 'guarantee_bank_guarantee_expiration_date',
            'advance_payment_required', 'advance_payment_paid', 'advance_payment_amount',
            'insurance_required', 'insurance_provided', 'insurance_expiration_date',
            'last_updated', 'user_updated'
        )
