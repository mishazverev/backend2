from rest_framework import serializers
from .models import *


class CategoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTag
        fields = ('id', 'category_tag_name', 'category_tag_description')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name', 'brand_description', 'brand_category_tag', 'retail_premise_type',
                  'needed_min_area', 'needed_max_area', 'needed_ceiling_height', 'needed_facade_length',
                  'needed_fitout_condition', 'needed_electric_capacity', 'needed_cooling_capacity',
                  'needed_water_supply', 'needed_additional_requirements')


class PremiseMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiseMain
        fields = (
            'id',
            'number',
            'premise_type',

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
                  'brands_id',
                  'description',

                  'needed_min_area',
                  'needed_max_area',
                  'needed_ceiling_height',
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


class TenantContractorContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantContractorContacts
        fields = (
            'id',
            'tenant_contractor_id',
            'contact_person_name',
            'contact_person_position',
            'contact_person_email',
            'contact_person_phone',
            'contact_person_mobile1',
            'contact_person_mobile2',
        )


class RentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContract
        fields = (
            'id',
            'rent_contract_number',
            'contract_signing_date',
            'contract_expiration_date',

            'premise_id',
            'contracted_area',
            'tenant_contractor_id',
            'brand',

            'rent_fee_per_sqm',
            'rent_fee_indexation_type',
            'rent_fee_indexation_fixed',
            'rent_fee_advance_payment_day',

            'turnover_fee',
            'turnover_fee_period',
            'turnover_data_providing_day',
            'turnover_fee_payment_day',

            'service_fee_per_sqm',
            'service_fee_indexation_type',
            'service_fee_indexation_fixed',
            'service_fee_advance_payment_day',

            'marketing_fee_per_sqm',
            'marketing_fee_indexation_type',
            'marketing_fee_indexation_fixed',
            'marketing_fee_advance_payment_day',

            'rent_start_date',
            'stop_billing_date',

            'act_of_transfer_date',
            'premise_return_date',

            # 'duration_years',
            # 'duration_months',
            # 'duration_days',

            'utilities_electricity_compensation_type',
            'utilities_electricity_counter_number',
            'utilities_electricity_compensation_fixed_fee',
            'utilities_electricity_compensation_fixed_indexation_type',
            'utilities_electricity_compensation_fixed_indexation_fixed',
            'utilities_electricity_compensation_payment_day',

            'utilities_cold_water_compensation_type',
            'utilities_cold_water_counter_number',
            'utilities_cold_water_compensation_fixed_fee',
            'utilities_cold_water_compensation_fixed_indexation_type',
            'utilities_cold_water_compensation_fixed_indexation_fixed',
            'utilities_cold_water_compensation_payment_day',

            'utilities_hot_water_compensation_type',
            'utilities_hot_water_counter_number',
            'utilities_hot_water_compensation_fixed_fee',
            'utilities_hot_water_compensation_fixed_indexation_type',
            'utilities_hot_water_compensation_fixed_indexation_fixed',
            'utilities_hot_water_compensation_payment_day',

            'utilities_gas_compensation_type',
            'utilities_gas_counter_number',
            'utilities_gas_compensation_fixed_fee',
            'utilities_gas_compensation_fixed_indexation_type',
            'utilities_gas_compensation_fixed_indexation_fixed',
            'utilities_gas_compensation_payment_day',

            'CA_utilities_compensation_type',
            'CA_utilities_compensation_fee_payment_day',
            'CA_utilities_compensation_fee_fixed',
            'CA_utilities_compensation_fixed_indexation_type',
            'CA_utilities_compensation_fee_fixed_indexation_type_fixed',

            'guarantee_deposit_type',
            'guarantee_deposit_amount',
            'guarantee_deposit_provided',
            'guarantee_deposit_contract_providing_date',
            'guarantee_bank_guarantee_expiration_date',

            # 'advance_payment_required',
            # 'advance_payment_paid',
            # 'advance_payment_amount',
            # 'advance_payment_contract_providing_date',

            'insurance_required',
            'insurance_contract_providing_date',
            'insurance_provided',
            'insurance_expiration_date',

            'last_updated',
            'user_updated'
        )
