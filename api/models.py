from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Building(models.Model):
    id = models.BigAutoField(primary_key=True)
    building_name = models.CharField(max_length=50, unique=True)
    address_postal_index = models.TextField(blank=True, null=True, max_length=10)
    address_country = models.CharField(blank=True, null=True, max_length=50)
    address_city = models.CharField(blank=True, null=True, max_length=50)
    address_street_number = models.CharField(blank=True, null=True, max_length=50)
    number_of_floors = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                           default=0)
    gba = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    gla = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    description = models.TextField(blank=True, null=True, max_length=500)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['building_name']

    def __str__(self):
        return self.building_name


class Counter(models.Model):
    id = models.BigAutoField(primary_key=True)
    counter_number = models.CharField(max_length=50, unique=True)
    counter_utility_type = models.CharField(max_length=50, unique=True)
    counter_description = models.CharField(null=True, max_length=200, blank=True)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['counter_number']

    def __str__(self):
        return self.counter_number


class BrandCategoryTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_tag_name = models.CharField(max_length=20, unique=True)
    category_tag_description = models.CharField(null=True, max_length=200)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['category_tag_name']

    def __str__(self):
        return self.category_tag_name


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(max_length=50, unique=True)
    brand_description = models.CharField(null=True, max_length=200, blank=True)
    brand_category_tag = models.ManyToManyField(BrandCategoryTag, null=True, blank=True)
    retail_premise_type = models.CharField(max_length=30, null=True, blank=True)
    needed_min_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    needed_max_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    needed_ceiling_height = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    needed_facade_length = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    needed_fitout_condition = models.BooleanField(default=False)
    needed_electric_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    needed_cooling_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    needed_water_supply = models.BooleanField(default=False)
    needed_additional_requirements = models.TextField(blank=True, null=True, max_length=500)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['brand_name']

    def __str__(self):
        return self.brand_name


class PremiseMain(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=7, unique=True)
    premise_type = models.CharField(max_length=50)

    floor = models.IntegerField(validators=[MinValueValidator(-20), MaxValueValidator(99)])
    measured_area = models.DecimalField(max_digits=8, decimal_places=2)
    measurement_date = models.DateField(null=True, default=datetime.now, auto_now=False, auto_now_add=False)
    contracted = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, max_length=500)

    ceiling_height = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    facade_length = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    fitout_condition = models.BooleanField(default=False)
    electric_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    cooling_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    water_supply = models.BooleanField(default=False)
    # UTILITIES COUNTERS
    # counter_id = models.ForeignKey(Counter, on_delete=models.DO_NOTHING, blank=True,
    #                                null=True, default='')

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.number


class TenantContractor(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    needed_premise_type = models.CharField(max_length=30)
    brands_id = models.ManyToManyField(Brand)
    description = models.TextField(blank=True, null=True, max_length=500)

    needed_min_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    needed_max_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    needed_ceiling_height = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    needed_fitout_condition = models.BooleanField(default=False)
    needed_electric_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    needed_cooling_capacity = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    needed_water_supply = models.BooleanField(default=False)
    needed_additional_requirements = models.TextField(blank=True, null=True, max_length=500)

    legal_name = models.CharField(max_length=100, null=True, blank=True)
    tax_id = models.BigIntegerField(unique=True, default=0, blank=True, null=True)
    signing_person_name = models.CharField(max_length=200, null=True, blank=True)
    signing_person_position = models.CharField(max_length=200, null=True, blank=True)
    legal_address = models.CharField(max_length=200, null=True, blank=True)
    postal_address = models.CharField(max_length=200, null=True, blank=True)

    kpp = models.CharField(max_length=9, null=True, blank=True)
    bik = models.CharField(max_length=9, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    current_account = models.CharField(max_length=40, null=True, blank=True)
    correspondent_account = models.CharField(max_length=40, null=True, blank=True)
    ogrn = models.CharField(max_length=15, null=True, blank=True)
    okpo = models.CharField(max_length=10, null=True, blank=True)
    registration_authority = models.CharField(max_length=100, null=True, blank=True)
    legal_entity_certificate_number = models.CharField(max_length=100, null=True, blank=True)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['company_name']

    def __str__(self):
        return self.company_name


class TenantContractorContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=models.CASCADE, null=True, default='')
    contact_person_name = models.CharField(max_length=100)
    contact_person_position = models.CharField(max_length=100, null=True, blank=True)
    contact_person_email = models.EmailField(null=True, blank=True)
    contact_person_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile1 = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile2 = models.CharField(max_length=100, null=True, blank=True)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['contact_person_name']

    def __str__(self):
        return self.contact_person_name


class RentContract(models.Model):
    # --- Main and commercial terms ---
    id = models.BigAutoField(primary_key=True)

    rent_contract_number = models.CharField(max_length=50)
    rent_contract_signing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    rent_contract_expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    building_id = models.ForeignKey(Building, on_delete=DO_NOTHING, null=True, default='')
    premise_id = models.ManyToManyField(PremiseMain)
    contracted_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=DO_NOTHING, null=True, default='')
    brand = models.ForeignKey(Brand, on_delete=DO_NOTHING, null=True)

    # --- Dates ---

    act_of_transfer_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    rent_start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)

    premise_return_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    stop_billing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    # Rental Payment
    fixed_rent_name = models.CharField(max_length=100, null=True, blank=True)

    class fixed_rent_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_period_types.choices,
        default=fixed_rent_calculation_period_types.MONTH, )

    class fixed_rent_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_payment_period_types.choices,
        default=fixed_rent_payment_period_types.MONTH, )

    class fixed_rent_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    fixed_rent_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_methods.choices,
        default=fixed_rent_calculation_methods.PER_SQM, )

    fixed_rent_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    fixed_rent_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class fixed_rent_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    fixed_rent_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_prepayment_or_postpayment_types.choices,
        default=fixed_rent_prepayment_or_postpayment_types.PREPAYMENT, )

    # In relevance with fixed_rent_payment_period - previous period day
    fixed_rent_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                         default=0)
    # Number of days after period is over
    fixed_rent_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                      default=0)

    class fixed_rent_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    fixed_rent_indexation_type = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        choices=fixed_rent_indexation_types.choices,
        default=fixed_rent_indexation_types.FIXED, )

    fixed_rent_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                      decimal_places=2, default=0)
    # Turnover fee

    turnover_fee_is_applicable = models.BooleanField(default=True)
    turnover_fee = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    class turnover_fee_periods(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    turnover_fee_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=turnover_fee_periods.choices,
        default=turnover_fee_periods.MONTH, )

    turnover_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)
    turnover_fee_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)

    # --- Utilities compensation - Common area (CA) ---
    CA_utilities_compensation_is_applicable = models.BooleanField(default=True)

    class CA_utilities_compensation_types(models.TextChoices):
        FIXED = 'Fixed'
        PROPORTIONAL_GLA = 'Proportional_to_GLA'
        PROPORTIONAL_LEASED = 'Proportional_to_leased_area'
        NONE = 'None'

    CA_utilities_compensation_type = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=CA_utilities_compensation_types.choices,
        default=CA_utilities_compensation_types.PROPORTIONAL_GLA, )

    class CA_utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    CA_utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fixed_indexation_types.choices,
        default=CA_utilities_compensation_fixed_indexation_types.FIXED, )

    CA_utilities_compensation_fee_fixed = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    CA_utilities_compensation_fee_fixed_indexation_type_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2,
                                                                                    default=0)

    class CA_utilities_compensation_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    CA_utilities_compensation_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fee_prepayment_or_postpayment_types.choices,
        default=CA_utilities_compensation_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    CA_utilities_compensation_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                            decimal_places=0,
                                                                            default=0)
    CA_utilities_compensation_fee_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                         decimal_places=0,
                                                                         default=0)

    # --- Guarantee deposit
    guarantee_deposit_required = models.BooleanField(default=True)
    guarantee_deposit_coverage_number_of_periods = models.DecimalField(null=True, max_digits=20, decimal_places=2)

    class guarantee_deposit_types(models.TextChoices):
        CASH = 'Cash'
        BANK_GUARANTEE = 'Bank_guarantee'
        CORPORATE_GUARANTEE = 'Corporate_guarantee'

    guarantee_deposit_type = models.CharField(
        null=True,
        max_length=25,
        choices=guarantee_deposit_types.choices,
        default=guarantee_deposit_types.CASH,
    )

    guarantee_deposit_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    guarantee_deposit_contract_providing_date = models.DateField(null=True, auto_now=False,
                                                                 auto_now_add=False)
    guarantee_deposit_actual_providing_date = models.DateField(null=True, auto_now=False,
                                                               auto_now_add=False)
    guarantee_bank_guarantee_expiration_date = models.DateField(null=True, auto_now=False,
                                                                auto_now_add=False)

    # --- Insurance
    insurance_required = models.BooleanField(default=True)
    insurance_contract_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    insurance_actual_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    insurance_expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['rent_contract_number']

    def __str__(self):
        return self.rent_contract_number


class AdditionalAgreement(models.Model):
    # --- Main and commercial terms ---
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')

    additional_agreement_number = models.CharField(max_length=50)
    additional_agreement_signing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    additional_agreement_expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    rent_contract_expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    premise_id = models.ManyToManyField(PremiseMain)
    contracted_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=DO_NOTHING, null=True, default='')
    brand = models.ForeignKey(Brand, on_delete=DO_NOTHING, null=True)

    # --- Dates ---
    rent_start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    stop_billing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    # Rental Payment
    class fixed_rent_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_period_types.choices,
        default=fixed_rent_calculation_period_types.MONTH, )

    class fixed_rent_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_payment_period_types.choices,
        default=fixed_rent_payment_period_types.MONTH, )

    class fixed_rent_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    fixed_rent_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_methods.choices,
        default=fixed_rent_calculation_methods.PER_SQM, )

    fixed_rent_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    fixed_rent_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class fixed_rent_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    fixed_rent_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_prepayment_or_postpayment_types.choices,
        default=fixed_rent_prepayment_or_postpayment_types.PREPAYMENT, )

    # In relevance with fixed_rent_payment_period - previous period day
    fixed_rent_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                         default=0)
    # Number of days after period is over
    fixed_rent_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                      default=0)

    class fixed_rent_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    fixed_rent_indexation_type = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        choices=fixed_rent_indexation_types.choices,
        default=fixed_rent_indexation_types.FIXED, )

    fixed_rent_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                      decimal_places=2, default=0)
    # Turnover fee

    turnover_fee_is_applicable = models.BooleanField(default=True)
    turnover_fee = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    class turnover_fee_periods(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    turnover_fee_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=turnover_fee_periods.choices,
        default=turnover_fee_periods.MONTH, )

    turnover_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)
    turnover_fee_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)

    # --- Utilities compensation - Common area (CA) ---
    CA_utilities_compensation_is_applicable = models.BooleanField(default=True)

    class CA_utilities_compensation_types(models.TextChoices):
        FIXED = 'Fixed'
        PROPORTIONAL_GLA = 'Proportional_to_GLA'
        PROPORTIONAL_LEASED = 'Proportional_to_leased_area'
        NONE = 'None'

    CA_utilities_compensation_type = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=CA_utilities_compensation_types.choices,
        default=CA_utilities_compensation_types.PROPORTIONAL_GLA, )

    class CA_utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    CA_utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fixed_indexation_types.choices,
        default=CA_utilities_compensation_fixed_indexation_types.FIXED, )

    CA_utilities_compensation_fee_fixed = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    CA_utilities_compensation_fee_fixed_indexation_type_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2,
                                                                                    default=0)

    class CA_utilities_compensation_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    CA_utilities_compensation_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fee_prepayment_or_postpayment_types.choices,
        default=CA_utilities_compensation_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    CA_utilities_compensation_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                            decimal_places=0,
                                                                            default=0)
    CA_utilities_compensation_fee_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                         decimal_places=0,
                                                                         default=0)

    # --- Guarantee deposit
    guarantee_deposit_required = models.BooleanField(default=True)
    guarantee_deposit_coverage_number_of_periods = models.DecimalField(null=True, max_digits=20, decimal_places=2)

    class guarantee_deposit_types(models.TextChoices):
        CASH = 'Cash'
        BANK_GUARANTEE = 'Bank_guarantee'
        CORPORATE_GUARANTEE = 'Corporate_guarantee'

    guarantee_deposit_type = models.CharField(
        null=True,
        max_length=25,
        choices=guarantee_deposit_types.choices,
        default=guarantee_deposit_types.CASH,
    )

    guarantee_deposit_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    guarantee_deposit_contract_providing_date = models.DateField(null=True, auto_now=False,
                                                                 auto_now_add=False)
    guarantee_deposit_actual_providing_date = models.DateField(null=True, auto_now=False,
                                                               auto_now_add=False)
    guarantee_bank_guarantee_expiration_date = models.DateField(null=True, auto_now=False,
                                                                auto_now_add=False)

    # --- Insurance
    insurance_required = models.BooleanField(default=True)
    insurance_contract_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    insurance_actual_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    insurance_expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['additional_agreement_number']

    def __str__(self):
        return self.additional_agreement_number


class RentContractPeriodicalFee(models.Model):
    # Is used for regular fixed fees (service fee, marketing fee, etc)

    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(AdditionalAgreement, on_delete=models.CASCADE,
                                                              null=True, blank=True, default='')
    periodical_fee_name = models.CharField(max_length=100)

    # Period of fee calculation
    class periodical_fee_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_calculation_period = models.CharField(
        null=True,
        max_length=20,
        choices=periodical_fee_calculation_period_types.choices,
        default=periodical_fee_calculation_period_types.MONTH, )

    # Period of fee payment
    class periodical_fee_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_payment_period_types.choices,
        default=periodical_fee_payment_period_types.MONTH, )

    # The way how periodical fee is calculated
    class periodical_fee_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    periodical_fee_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_calculation_methods.choices,
        default=periodical_fee_calculation_methods.PER_SQM, )

    # Types of periodical fee calculation
    periodical_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    periodical_fee_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class periodical_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    periodical_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_prepayment_or_postpayment_types.choices,
        default=periodical_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    # In relevance with periodical_fee_payment_period - previous period day
    periodical_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                             default=0)
    # Number of days after period is over
    periodical_fee_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                          default=0)

    # Periodical fee indexation
    class periodical_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    periodical_fee_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_indexation_types.choices,
        default=periodical_fee_indexation_types.FIXED, )

    periodical_payment_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                              decimal_places=2, default=0)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['periodical_fee_name']

    def __str__(self):
        return self.periodical_fee_name


class RentContractOneTimeFee(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(AdditionalAgreement, on_delete=models.CASCADE,
                                                              null=True, blank=True, default='')
    one_time_fee_name = models.CharField(max_length=100)

    # The way how one-time fee is calculated
    class one_time_fee_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    one_time_fee_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=one_time_fee_calculation_methods.choices,
        default=one_time_fee_calculation_methods.PER_SQM, )

    # The term of one-time fee payment

    class one_time_fee_payment_terms(models.TextChoices):
        FIXED_DATE = 'Fixed_date'
        TRIGGERING_EVENT_DATE = 'Triggering_event_date'
        NOT_FIXED = 'Not_fixed'

    one_time_fee_payment_term = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=one_time_fee_payment_terms.choices,
        default=one_time_fee_payment_terms.FIXED_DATE, )

    # Type of events triggering one-time fee payment
    class one_time_fee_payment_triggering_events(models.TextChoices):
        CONTRACT_SIGNING_DATE = 'Contract_signing_date'
        ACT_OF_TRANSFER_DATE = 'Premise_transfer_date'
        RENT_START_DATE = 'Start_of_commercial_activity'

    one_time_fee_payment_triggering_event = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=one_time_fee_payment_triggering_events.choices,
        default=one_time_fee_payment_triggering_events.ACT_OF_TRANSFER_DATE, )

    # One-time fee amount
    one_time_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    one_time_fee_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    # One-time fee payment dated
    one_time_fee_contract_payment_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    one_time_fee_contract_triggering_event_related_payment_day = models.DecimalField(null=True, blank=True,
                                                                                     max_digits=4,
                                                                                     decimal_places=0,
                                                                                     default=0)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['one_time_fee_name']

    def __str__(self):
        return self.one_time_fee_name


class RentContractUtilityFee(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(
        AdditionalAgreement,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default='')
    utility_name = models.CharField(max_length=100)

    # usually -  USING COUNTER
    class compensation_types(models.TextChoices):
        USING_COUNTER = 'Using_counter'
        FIXED = 'Fixed'
        NONE = 'None'

    compensation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_types.choices,
        default=compensation_types.USING_COUNTER, )

    # IF BY COUNTERS ONLY
    # counter_id = models.ForeignKey(Counter, on_delete=models.DO_NOTHING, blank=True,
    #                                       null=True, default='')

    # IF FIXED COMPENSATION ONLY - Period of fixed utility compensation payment (usually - one month)
    class compensation_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    # IF FIXED COMPENSATION ONLY - Period of fixed utility compensation payment (usually - one month)
    compensation_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_calculation_period_types.choices,
        default=compensation_calculation_period_types.MONTH, )

    # BOTH USING COUNTER and FIXED Period of utility compensation payment (usually - one month)
    class compensation_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    # BOTH USING COUNTER and FIXED Period of utility compensation payment (usually - one month)
    compensation_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_payment_period_types.choices,
        default=compensation_payment_period_types.MONTH, )

    # IF FIXED COMPENSATION ONLY - regular fixed utility compensation fee amount
    compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    # IF FIXED COMPENSATION ONLY - indexation type of fixed utility compensation
    class compensation_fixed_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    # IF FIXED COMPENSATION ONLY - indexation type of fixed utility compensation
    compensation_fixed_fee_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_fixed_fee_indexation_types.choices,
        default=compensation_fixed_fee_indexation_types.FIXED, )

    # IF FIXED COMPENSATION ONLY - annual indexation % of fixed utility compensation
    compensation_fixed_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                  decimal_places=2, default=0)

    class compensation_fixed_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    compensation_fixed_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_fixed_fee_prepayment_or_postpayment_types.choices,
        default=compensation_fixed_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    # IF FIXED COMPENSATION ONLY - In relevance with compensation_payment_period_types - previous period day
    compensation_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                           decimal_places=0,
                                                           default=0)
    # IF COMPENSATION USING COUNTER ONLY - Limited number of days after period is over to provide counter data
    compensation_counter_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                  decimal_places=0,
                                                                  default=0)
    # BOTH USING COUNTER and FIXED - Limited number of days after period is over to make payment
    compensation_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                        default=0)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['utility_name']

    def __str__(self):
        return self.utility_name


class RentContractSetup(models.Model):
    # --- Main and commercial terms ---

    id = models.BigAutoField(primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, default='')

    # Rental Payment
    fixed_rent_name = models.CharField(max_length=100, null=True, blank=True)

    class fixed_rent_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_period_types.choices,
        default=fixed_rent_calculation_period_types.MONTH, )

    class fixed_rent_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_payment_period_types.choices,
        default=fixed_rent_payment_period_types.MONTH, )

    class fixed_rent_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    fixed_rent_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_methods.choices,
        default=fixed_rent_calculation_methods.PER_SQM, )

    # fixed_rent_step_payment = models

    fixed_rent_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    fixed_rent_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class fixed_rent_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    fixed_rent_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_prepayment_or_postpayment_types.choices,
        default=fixed_rent_prepayment_or_postpayment_types.PREPAYMENT, )

    # In relevance with fixed_rent_payment_period - previous period day
    fixed_rent_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                         default=0)
    # Number of days after period is over
    fixed_rent_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                      default=0)

    class fixed_rent_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    fixed_rent_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_indexation_types.choices,
        default=fixed_rent_indexation_types.FIXED, )

    fixed_rent_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                      decimal_places=2, default=0)
    # Turnover fee

    turnover_fee_is_applicable = models.BooleanField(default=True)
    turnover_fee = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    class turnover_fee_periods(models.TextChoices):
        MONTH1 = 'Month'
        MONTH3 = '3_months'
        MONTH6 = '6_months'
        MONTH12 = 'Year'

    turnover_fee_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=turnover_fee_periods.choices,
        default=turnover_fee_periods.MONTH1, )

    turnover_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)
    turnover_fee_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)

    # --- Utilities compensation - Common area (CA) ---
    CA_utilities_compensation_is_applicable = models.BooleanField(default=True)

    class CA_utilities_compensation_types(models.TextChoices):
        FIXED = 'Fixed'
        PROPORTIONAL_GLA = 'Proportional_to_GLA'
        PROPORTIONAL_LEASED = 'Proportional_to_leased_area'
        NONE = 'None'

    CA_utilities_compensation_type = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=CA_utilities_compensation_types.choices,
        default=CA_utilities_compensation_types.PROPORTIONAL_GLA, )

    class CA_utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    CA_utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fixed_indexation_types.choices,
        default=CA_utilities_compensation_fixed_indexation_types.FIXED, )

    CA_utilities_compensation_fee_fixed = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    CA_utilities_compensation_fee_fixed_indexation_type_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2,
                                                                                    default=0)

    class CA_utilities_compensation_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    CA_utilities_compensation_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=CA_utilities_compensation_fee_prepayment_or_postpayment_types.choices,
        default=CA_utilities_compensation_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    CA_utilities_compensation_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                            decimal_places=0,
                                                                            default=0)
    CA_utilities_compensation_fee_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                         decimal_places=0,
                                                                         default=0)

    # --- Guarantee deposit
    guarantee_deposit_required = models.BooleanField(default=True)
    guarantee_deposit_coverage_number_of_periods = models.DecimalField(null=True, max_digits=20, decimal_places=2)

    # --- Insurance
    insurance_required = models.BooleanField(default=True)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class RentContractPeriodicalFeeSetup(models.Model):
    # Is used for regular fixed fees (service fee, marketing fee, etc)

    id = models.BigAutoField(primary_key=True)
    rent_contract_setup_id = models.ForeignKey(RentContractSetup, on_delete=models.CASCADE, null=True, default='')
    periodical_fee_name = models.CharField(max_length=100, null=True, blank=True)

    # Period of fee calculation
    class periodical_fee_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_calculation_period_types.choices,
        default=periodical_fee_calculation_period_types.MONTH, )

    # Period of fee payment
    class periodical_fee_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_payment_period_types.choices,
        default=periodical_fee_payment_period_types.MONTH, )

    # The way how periodical fee is calculated
    class periodical_fee_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    periodical_fee_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_calculation_methods.choices,
        default=periodical_fee_calculation_methods.PER_SQM, )

    # Types of periodical fee calculation
    periodical_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    periodical_fee_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class periodical_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    periodical_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_prepayment_or_postpayment_types.choices,
        default=periodical_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    # In relevance with periodical_fee_payment_period - previous period day
    periodical_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                             default=0)
    # Number of days after period is over
    periodical_fee_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                          default=0)

    # Periodical fee indexation
    class periodical_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    periodical_fee_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_indexation_types.choices,
        default=periodical_fee_indexation_types.FIXED, )

    periodical_payment_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                              decimal_places=2, default=0)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['periodical_fee_name']

    def __str__(self):
        return self.periodical_fee_name


class RentContractOneTimeFeeSetup(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_setup_id = models.ForeignKey(RentContractSetup, on_delete=models.CASCADE, null=True, default='')
    one_time_fee_name = models.CharField(max_length=100, null=True, blank=True)

    # The way how one-time fee is calculated
    class one_time_fee_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    one_time_fee_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=one_time_fee_calculation_methods.choices,
        default=one_time_fee_calculation_methods.PER_SQM, )

    # The term of one-time fee payment

    class one_time_fee_payment_terms(models.TextChoices):
        FIXED_DATE = 'Fixed_date'
        TRIGGERING_EVENT_DATE = 'Triggering_event_date'
        NOT_FIXED = 'Not_fixed'

    one_time_fee_payment_term = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=one_time_fee_payment_terms.choices,
        default=one_time_fee_payment_terms.FIXED_DATE, )

    # Type of events triggering one-time fee payment
    class one_time_fee_payment_triggering_events(models.TextChoices):
        CONTRACT_SIGNING_DATE = 'Contract_signing_date'
        ACT_OF_TRANSFER_DATE = 'Premise_transfer_date'
        RENT_START_DATE = 'Start_of_commercial_activity'

    one_time_fee_payment_triggering_event = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=one_time_fee_payment_triggering_events.choices,
        default=one_time_fee_payment_triggering_events.ACT_OF_TRANSFER_DATE, )

    # One-time fee amount
    one_time_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    one_time_fee_total_payment = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    # One-time fee payment dated
    one_time_fee_contract_payment_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    one_time_fee_contract_triggering_event_related_payment_day = models.DecimalField(null=True, blank=True,
                                                                                     max_digits=2,
                                                                                     decimal_places=0,
                                                                                     default=0)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['one_time_fee_name']

    def __str__(self):
        return self.one_time_fee_name


class RentContractUtilityFeeSetup(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_setup_id = models.ForeignKey(RentContractSetup, on_delete=models.CASCADE, null=True, default='')
    utility_name = models.CharField(max_length=100, null=True, blank=True)

    # usually -  USING COUNTER
    class compensation_types(models.TextChoices):
        USING_COUNTER = 'Using_counter'
        FIXED = 'Fixed'
        NONE = 'None'

    compensation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_types.choices,
        default=compensation_types.USING_COUNTER, )

    # IF FIXED COMPENSATION ONLY - Period of fixed utility compensation payment (usually - one month)
    class compensation_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    # IF FIXED COMPENSATION ONLY - Period of fixed utility compensation payment (usually - one month)
    compensation_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_calculation_period_types.choices,
        default=compensation_calculation_period_types.MONTH, )

    # BOTH USING COUNTER and FIXED Period of utility compensation payment (usually - one month)
    class compensation_payment_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    # BOTH USING COUNTER and FIXED Period of utility compensation payment (usually - one month)
    compensation_payment_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_payment_period_types.choices,
        default=compensation_payment_period_types.MONTH, )

    # IF FIXED COMPENSATION ONLY - regular fixed utility compensation fee amount
    compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    # IF FIXED COMPENSATION ONLY - indexation type of fixed utility compensation
    class compensation_fixed_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NON_INDEXABLE = 'Non_Indexable'

    # IF FIXED COMPENSATION ONLY - indexation type of fixed utility compensation
    compensation_fixed_fee_indexation_type = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_fixed_fee_indexation_types.choices,
        default=compensation_fixed_fee_indexation_types.FIXED, )
    # IF FIXED COMPENSATION ONLY - annual indexation % of fixed utility compensation
    compensation_fixed_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                  decimal_places=2, default=0)

    class compensation_fixed_fee_prepayment_or_postpayment_types(models.TextChoices):
        PREPAYMENT = 'Prepayment'
        POSTPAYMENT = 'Postpayment'

    compensation_fixed_fee_prepayment_or_postpayment = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=compensation_fixed_fee_prepayment_or_postpayment_types.choices,
        default=compensation_fixed_fee_prepayment_or_postpayment_types.PREPAYMENT, )

    # IF FIXED COMPENSATION ONLY - In relevance with compensation_payment_period_types - previous period day
    compensation_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                           decimal_places=0,
                                                           default=0)
    # IF COMPENSATION USING COUNTER ONLY - Limited number of days after period is over to provide counter data
    compensation_counter_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                  decimal_places=0,
                                                                  default=0)
    # BOTH USING COUNTER and FIXED - Limited number of days after period is over to make payment
    compensation_post_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                        default=0)
    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['utility_name']

    def __str__(self):
        return self.utility_name


class FixedRentStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(AdditionalAgreement, on_delete=models.CASCADE,
                                                              null=True, blank=True, default='')
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    fixed_rent_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class fixed_rent_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_period_types.choices,
        default=fixed_rent_calculation_period_types.MONTH, )

    class fixed_rent_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    fixed_rent_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_calculation_methods.choices,
        default=fixed_rent_calculation_methods.PER_SQM, )

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class FixedRentIndexationStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(AdditionalAgreement, on_delete=models.CASCADE,
                                                              null=True, blank=True, default='')
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    fixed_rent_indexation_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class fixed_rent_indexation_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    fixed_rent_indexation_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=fixed_rent_indexation_calculation_period_types.choices,
        default=fixed_rent_indexation_calculation_period_types.MONTH, )

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class TurnoverFeeStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    rent_contract_id = models.ForeignKey(RentContract, on_delete=models.CASCADE, null=True, default='')
    rent_contract_additional_agreement_id = models.ForeignKey(AdditionalAgreement, on_delete=models.CASCADE,
                                                              null=True, blank=True, default='')
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    turnover_fee_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class turnover_fee_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    turnover_fee_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=turnover_fee_calculation_period_types.choices,
        default=turnover_fee_calculation_period_types.MONTH, )

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class PeriodicalFeeStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    periodical_fee_id = models.ForeignKey(RentContractPeriodicalFee, on_delete=models.CASCADE, null=True, default='')
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    periodical_fee_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class periodical_fee_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_calculation_period_types.choices,
        default=periodical_fee_calculation_period_types.MONTH, )

    # The way how periodical fee is calculated
    class periodical_fee_calculation_methods(models.TextChoices):
        PER_SQM = 'Per_sqm'
        TOTAL = 'Total'

    periodical_fee_calculation_method = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_calculation_methods.choices,
        default=periodical_fee_calculation_methods.PER_SQM, )

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class PeriodicalFeeIndexationStep(models.Model):
    id = models.BigAutoField(primary_key=True)
    periodical_fee_id = models.ForeignKey(RentContractPeriodicalFee, on_delete=models.CASCADE, null=True, default='')

    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    periodical_fee_indexation_amount = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class periodical_fee_indexation_calculation_period_types(models.TextChoices):
        DAY = 'Day'
        WEEK = 'Week'
        MONTH = 'Month'
        MONTHS3 = '3_months'
        MONTHS6 = '6_months'
        YEAR = 'Year'

    periodical_fee_indexation_calculation_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=periodical_fee_indexation_calculation_period_types.choices,
        default=periodical_fee_indexation_calculation_period_types.MONTH, )

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
