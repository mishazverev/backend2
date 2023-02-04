from rest_framework import serializers
from .models import *


class BrandCategoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategoryTag
        fields = ('id',
                  'category_tag_name',
                  'category_tag_description',
                  'last_updated',
                  'user_updated'
                  )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand_name', 'brand_description', 'brand_category_tag', 'retail_premise_type',
                  'needed_min_area', 'needed_max_area', 'needed_ceiling_height', 'needed_facade_length',
                  'needed_fitout_condition', 'needed_electric_capacity', 'needed_cooling_capacity',
                  'needed_water_supply', 'needed_additional_requirements', 'last_updated', 'user_updated')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = (
            'id',
            'building_name',
            'address_postal_index',
            'address_country',
            'address_city',
            'address_street_number',
            'number_of_floors',
            'gba',
            'gla',
            'description',
            'last_updated',
            'user_updated'
        )


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
            # 'counter_id',
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
            'last_updated',
            'user_updated'
        )


class RentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContract
        fields = (
            'id',

            'rent_contract_number',
            'rent_contract_signing_date',
            'rent_contract_expiration_date',

            'building_id',
            'premise_id',
            'contracted_area',
            'tenant_contractor_id',
            'brand',

            'act_of_transfer_date',
            'rent_start_date',
            'premise_return_date',
            'stop_billing_date',

            'fixed_rent_name',
            'fixed_rent_calculation_period',
            'fixed_rent_payment_period',
            'fixed_rent_calculation_method',

            'fixed_rent_per_sqm',
            'fixed_rent_total_payment',
            'fixed_rent_prepayment_or_postpayment',

            'fixed_rent_advance_payment_day',
            'fixed_rent_post_payment_day',
            'fixed_rent_indexation_type',
            'fixed_rent_indexation_fixed',

            'turnover_fee_is_applicable',
            'turnover_fee',
            'turnover_fee_period',
            'turnover_data_providing_day',
            'turnover_fee_payment_day',

            'CA_utilities_compensation_is_applicable',
            'CA_utilities_compensation_type',

            'CA_utilities_compensation_fixed_indexation_type',
            'CA_utilities_compensation_fee_fixed',
            'CA_utilities_compensation_fee_fixed_indexation_type_fixed',

            'CA_utilities_compensation_fee_prepayment_or_postpayment',
            'CA_utilities_compensation_fee_advance_payment_day',
            'CA_utilities_compensation_fee_post_payment_day',

            'guarantee_deposit_required',
            'guarantee_deposit_coverage_number_of_periods',
            'guarantee_deposit_type',
            'guarantee_deposit_amount',
            'guarantee_deposit_contract_providing_date',
            'guarantee_deposit_actual_providing_date',
            'guarantee_bank_guarantee_expiration_date',

            'insurance_required',
            'insurance_contract_providing_date',
            'insurance_actual_providing_date',
            'insurance_expiration_date',

            'last_updated',
            'user_updated'
        )


class AdditionalAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalAgreement
        fields = (
            'id',
            'rent_contract_id',
            'additional_agreement_number',
            'additional_agreement_signing_date',
            'additional_agreement_expiration_date',
            'rent_contract_expiration_date',

            'premise_id',
            'contracted_area',
            'tenant_contractor_id',
            'brand',
            'rent_start_date',
            'stop_billing_date',
            'fixed_rent_calculation_period',
            'fixed_rent_payment_period',
            'fixed_rent_calculation_method',
            'fixed_rent_per_sqm',
            'fixed_rent_total_payment',
            'fixed_rent_prepayment_or_postpayment',
            'fixed_rent_advance_payment_day',
            'fixed_rent_post_payment_day',
            'fixed_rent_indexation_type',
            'fixed_rent_indexation_fixed',
            'turnover_fee_is_applicable',
            'turnover_fee',
            'turnover_fee_period',
            'turnover_data_providing_day',
            'turnover_fee_payment_day',
            'CA_utilities_compensation_is_applicable',
            'CA_utilities_compensation_type',
            'CA_utilities_compensation_fixed_indexation_type',
            'CA_utilities_compensation_fee_fixed',
            'CA_utilities_compensation_fee_fixed_indexation_type_fixed',
            'CA_utilities_compensation_fee_prepayment_or_postpayment',
            'CA_utilities_compensation_fee_advance_payment_day',
            'CA_utilities_compensation_fee_post_payment_day',
            'guarantee_deposit_required',
            'guarantee_deposit_coverage_number_of_periods',
            'guarantee_deposit_type',
            'guarantee_deposit_amount',
            'guarantee_deposit_contract_providing_date',
            'guarantee_deposit_actual_providing_date',
            'guarantee_bank_guarantee_expiration_date',
            'insurance_required',
            'insurance_contract_providing_date',
            'insurance_actual_providing_date',
            'insurance_expiration_date',
            'last_updated',
            'user_updated',
        )


class RentContractPeriodicalFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractPeriodicalFee
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',
            'periodical_fee_name',
            'periodical_fee_calculation_period',
            'periodical_fee_payment_period',
            'periodical_fee_calculation_method',
            'periodical_fee_per_sqm',
            'periodical_fee_total_payment',
            'periodical_fee_prepayment_or_postpayment',
            'periodical_fee_advance_payment_day',
            'periodical_fee_post_payment_day',
            'periodical_fee_indexation_type',
            'periodical_payment_indexation_fixed',
            'last_updated',
            'user_updated',
        )


class RentContractOneTimeFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractOneTimeFee
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',
            'one_time_fee_name',
            'one_time_fee_calculation_method',
            'one_time_fee_payment_term',
            'one_time_fee_payment_triggering_event',
            'one_time_fee_per_sqm',
            'one_time_fee_total_payment',
            'one_time_fee_contract_payment_date',
            'one_time_fee_contract_triggering_event_related_payment_day',
            'last_updated',
            'user_updated',
        )


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = (
            'id',
            'counter_number',
            'counter_utility_type',
            'counter_description',
            'last_updated',
            'user_updated',
        )


class RentContractUtilityFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractUtilityFee
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',
            'utility_name',
            'compensation_type',
            # 'counter_id',
            'compensation_calculation_period',
            'compensation_payment_period',
            'compensation_fixed_fee',
            'compensation_fixed_fee_indexation_type',
            'compensation_fixed_fee_indexation_fixed',
            'compensation_fixed_fee_prepayment_or_postpayment',
            'compensation_advance_payment_day',
            'compensation_counter_data_providing_day',
            'compensation_post_payment_day',
            'last_updated',
            'user_updated',
        )


class RentContractSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractSetup
        fields = (
            'id',
            'building_id',

            'fixed_rent_name',

            'fixed_rent_calculation_period',
            'fixed_rent_payment_period',

            'fixed_rent_calculation_method',
            'fixed_rent_per_sqm',
            'fixed_rent_total_payment',

            'fixed_rent_prepayment_or_postpayment',
            'fixed_rent_advance_payment_day',
            'fixed_rent_post_payment_day',
            'fixed_rent_indexation_type',
            'fixed_rent_indexation_fixed',

            'turnover_fee_is_applicable',
            'turnover_fee',
            'turnover_fee_period',
            'turnover_data_providing_day',
            'turnover_fee_payment_day',

            'CA_utilities_compensation_is_applicable',
            'CA_utilities_compensation_type',
            'CA_utilities_compensation_fixed_indexation_type',

            'CA_utilities_compensation_fee_fixed',
            'CA_utilities_compensation_fee_fixed_indexation_type_fixed',

            'CA_utilities_compensation_fee_prepayment_or_postpayment',
            'CA_utilities_compensation_fee_advance_payment_day',
            'CA_utilities_compensation_fee_post_payment_day',

            'guarantee_deposit_required',
            'guarantee_deposit_coverage_number_of_periods',

            'insurance_required',

            'last_updated',
            'user_updated'
        )


class RentContractPeriodicalFeeSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractPeriodicalFeeSetup
        fields = (
            'id',
            'rent_contract_setup_id',
            'periodical_fee_name',
            'periodical_fee_calculation_period',
            'periodical_fee_payment_period',
            'periodical_fee_calculation_method',
            'periodical_fee_per_sqm',
            'periodical_fee_total_payment',
            'periodical_fee_prepayment_or_postpayment',
            'periodical_fee_advance_payment_day',
            'periodical_fee_post_payment_day',
            'periodical_fee_indexation_type',
            'periodical_payment_indexation_fixed',
            'last_updated',
            'user_updated',
        )


class RentContractOneTimeFeeSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractOneTimeFeeSetup
        fields = (
            'id',
            'rent_contract_setup_id',
            'one_time_fee_name',
            'one_time_fee_calculation_method',
            'one_time_fee_payment_term',
            'one_time_fee_payment_triggering_event',
            'one_time_fee_per_sqm',
            'one_time_fee_total_payment',
            'one_time_fee_contract_payment_date',
            'one_time_fee_contract_triggering_event_related_payment_day',
            'last_updated',
            'user_updated',
        )


class RentContractUtilityFeeSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentContractUtilityFeeSetup
        fields = (
            'id',
            'rent_contract_setup_id',
            'utility_name',
            'compensation_type',
            'compensation_calculation_period',
            'compensation_payment_period',
            'compensation_fixed_fee',
            'compensation_fixed_fee_indexation_type',
            'compensation_fixed_fee_indexation_fixed',
            'compensation_fixed_fee_prepayment_or_postpayment',
            'compensation_advance_payment_day',
            'compensation_counter_data_providing_day',
            'compensation_post_payment_day',
            'last_updated',
            'user_updated',
        )


class FixedRentStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedRentStep
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',

            'start_date',
            'expiration_date',
            'fixed_rent_amount',
            'fixed_rent_calculation_period',
            'fixed_rent_calculation_method',
            'last_updated',
            'user_updated',
        )


class FixedRentIndexationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedRentIndexationStep
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',

            'start_date',
            'expiration_date',
            'fixed_rent_indexation_amount',
            'fixed_rent_indexation_calculation_period',
            'last_updated',
            'user_updated',
        )


class TurnoverFeeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnoverFeeStep
        fields = (
            'id',
            'rent_contract_id',
            'rent_contract_additional_agreement_id',

            'start_date',
            'expiration_date',
            'turnover_fee_amount',
            'turnover_fee_calculation_period',
            'last_updated',
            'user_updated',
        )


class PeriodicalFeeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicalFeeStep
        fields = (
            'id',
            'periodical_fee_id',
            'start_date',
            'expiration_date',
            'periodical_fee_amount',
            'periodical_fee_calculation_period',
            'periodical_fee_calculation_method',
            'last_updated',
            'user_updated',
        )


class PeriodicalFeeIndexationStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicalFeeIndexationStep
        fields = (
            'id',
            'periodical_fee_id',
            'start_date',
            'expiration_date',
            'periodical_fee_indexation_amount',
            'periodical_fee_indexation_calculation_period',
            'last_updated',
            'user_updated',
        )
