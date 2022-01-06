from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class CategoryTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_tag_name = models.CharField(max_length=20, unique=True)
    category_tag_description = models.CharField(null=True, max_length=200)

    class Meta:
        ordering = ['category_tag_name']

    def __str__(self):
        return self.category_tag_name


class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(max_length=50, unique=True)
    brand_description = models.CharField(null=True, max_length=200)
    brand_category_tag = models.ManyToManyField(CategoryTag, null=True, blank=True)

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

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['number']


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


class TenantContractorContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=models.CASCADE, null=True, default='')
    contact_person_name = models.CharField(max_length=100, null=True, blank=True)
    contact_person_position = models.CharField(max_length=100, null=True, blank=True)
    contact_person_email = models.EmailField(null=True, blank=True)
    contact_person_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile1 = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile2 = models.CharField(max_length=100, null=True, blank=True)


class RentContract(models.Model):
    # --- Main and commercial terms ---

    id = models.BigAutoField(primary_key=True)
    rent_contract_number = models.CharField(max_length=50, null=True, blank=True)
    contract_signing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    contract_expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    premise_id = models.ManyToManyField(PremiseMain)
    contracted_area = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=DO_NOTHING, null=True, default='')
    brand = models.ForeignKey(Brand, on_delete=DO_NOTHING, null=True)

    rent_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    rent_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)

    class rent_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    rent_fee_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=rent_fee_indexation_types.choices,
        default=rent_fee_indexation_types.CPI, )

    rent_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    turnover_fee = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    class turnover_fee_periods(models.TextChoices):
        MONTH1 = '1_month'
        MONTH3 = '3_months'
        MONTH6 = '6_months'
        MONTH12 = '12_months'

    turnover_fee_period = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=turnover_fee_periods.choices,
        default=turnover_fee_periods.MONTH1, )

    turnover_data_providing_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)
    turnover_fee_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0, default=0)

    service_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    service_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                          default=0)

    class service_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    service_fee_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=service_fee_indexation_types.choices,
        default=service_fee_indexation_types.FIXED, )
    service_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    marketing_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    marketing_fee_advance_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                            default=0)

    class marketing_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    marketing_fee_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=marketing_fee_indexation_types.choices,
        default=marketing_fee_indexation_types.FIXED, )

    marketing_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)

    # --- Dates ---

    act_of_transfer_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    rent_start_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)

    premise_return_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    stop_billing_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    # duration_years = models.IntegerField(null=True)
    # duration_months = models.IntegerField(null=True)
    # duration_days = models.IntegerField(null=True)

    # --- Utilities compensation - consumed by tenant ---

    # ----- Utilities compensation - consumed by tenant - electricity ---

    class utilities_electricity_compensation_types(models.TextChoices):
        BY_COUNTERS = 'By counters'
        FIXED = 'Fixed'
        NONE = 'None'

    utilities_electricity_compensation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_electricity_compensation_types.choices,
        default=utilities_electricity_compensation_types.BY_COUNTERS, )

    utilities_electricity_counter_number = models.CharField(max_length=100, null=True, blank=True)
    utilities_electricity_compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2,
                                                                       default=0)

    class utilities_electricity_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    utilities_electricity_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_electricity_compensation_fixed_indexation_types.choices,
        default=utilities_electricity_compensation_fixed_indexation_types.FIXED, )

    utilities_electricity_compensation_fixed_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2, default=0)

    utilities_electricity_compensation_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                         decimal_places=0, default=0)

    # ----- Utilities compensation - consumed by tenant - cold water ---

    class utilities_cold_water_compensation_types(models.TextChoices):
        BY_COUNTERS = 'By counters'
        FIXED = 'Fixed'
        NONE = 'None'

    utilities_cold_water_compensation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_cold_water_compensation_types.choices,
        default=utilities_cold_water_compensation_types.BY_COUNTERS, )

    utilities_cold_water_counter_number = models.CharField(max_length=100, null=True, blank=True)
    utilities_cold_water_compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2,
                                                                      default=0)

    class utilities_cold_water_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    utilities_cold_water_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_cold_water_compensation_fixed_indexation_types.choices,
        default=utilities_cold_water_compensation_fixed_indexation_types.FIXED, )

    utilities_cold_water_compensation_fixed_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                   decimal_places=2, default=0)

    utilities_cold_water_compensation_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                        decimal_places=0, default=0)

    # ----- Utilities compensation - consumed by tenant - hot water ---

    class utilities_hot_water_compensation_types(models.TextChoices):
        BY_COUNTERS = 'By counters'
        FIXED = 'Fixed'
        NONE = 'None'

    utilities_hot_water_compensation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_hot_water_compensation_types.choices,
        default=utilities_hot_water_compensation_types.BY_COUNTERS, )

    utilities_hot_water_counter_number = models.CharField(max_length=100, null=True, blank=True)
    utilities_hot_water_compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2,
                                                                     default=0)

    class utilities_hot_water_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    utilities_hot_water_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_hot_water_compensation_fixed_indexation_types.choices,
        default=utilities_hot_water_compensation_fixed_indexation_types.FIXED, )

    utilities_hot_water_compensation_fixed_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                  decimal_places=2, default=0)

    utilities_hot_water_compensation_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                       decimal_places=0, default=0)

    # ----- Utilities compensation - consumed by tenant - gas ---

    class utilities_gas_compensation_types(models.TextChoices):
        BY_COUNTERS = 'By counters'
        FIXED = 'Fixed'
        NONE = 'None'

    utilities_gas_compensation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_gas_compensation_types.choices,
        default=utilities_gas_compensation_types.BY_COUNTERS, )

    utilities_gas_counter_number = models.CharField(max_length=100, null=True, blank=True)
    utilities_gas_compensation_fixed_fee = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class utilities_gas_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    utilities_gas_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_gas_compensation_fixed_indexation_types.choices,
        default=utilities_gas_compensation_fixed_indexation_types.FIXED, )

    utilities_gas_compensation_fixed_indexation_fixed = models.DecimalField(null=True, max_digits=4,
                                                                            decimal_places=2, default=0)

    utilities_gas_compensation_payment_day = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=0,
                                                                 default=0)

    # --- Utilities compensation - Common area (CA) ---

    class CA_utilities_compensation_types(models.TextChoices):
        FIXED = 'Fixed'
        PROPORTIONAL_LEASED = 'Proportional to leased area'
        PROPORTIONAL_GLA = 'Proportional to GLA'
        NONE = 'None'

    CA_utilities_compensation_type = models.CharField(
        null=True,
        max_length=50,
        choices=CA_utilities_compensation_types.choices,
        default=CA_utilities_compensation_types.PROPORTIONAL_LEASED, )

    class CA_utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'
        NONINDEXABLE = 'NonIndexable'

    CA_utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=20,
        choices=CA_utilities_compensation_fixed_indexation_types.choices,
        default=CA_utilities_compensation_fixed_indexation_types.FIXED, )

    CA_utilities_compensation_fee_fixed = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    CA_utilities_compensation_fee_fixed_indexation_type_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2,
                                                                                    default=0)

    CA_utilities_compensation_fee_payment_day = models.DecimalField(null=True, blank=True, max_digits=2,
                                                                    decimal_places=0, default=0)

    # --- Guarantee deposit

    class guarantee_deposit_types(models.TextChoices):
        CASH = 'Cash'
        BANK_GUARANTEE = 'Bank guarantee'
        CORPORATE_GUARANTEE = 'Corporate guarantee'
        NONE = 'None'

    guarantee_deposit_type = models.CharField(
        null=True,
        max_length=25,
        choices=guarantee_deposit_types.choices,
        default=guarantee_deposit_types.CASH,
    )

    guarantee_deposit_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    guarantee_deposit_provided = models.BooleanField(default=False)
    guarantee_deposit_contract_providing_date = models.DateField(null=True, auto_now=False,
                                                                 auto_now_add=False)
    guarantee_bank_guarantee_expiration_date = models.DateField(null=True, auto_now=False,
                                                                auto_now_add=False)

    # --- Insurance
    class insurance_required_options(models.TextChoices):
        REQUIRED = 'Required'
        NOT_REQUIRED = 'Not required'

    insurance_required = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        choices=insurance_required_options.choices,
        default=insurance_required_options.REQUIRED,
    )

    insurance_contract_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    insurance_provided = models.BooleanField(null=True, default=None)
    insurance_expiration_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)

    # --- Advance payment

    class advance_payment_required_options(models.TextChoices):
        REQUIRED = 'Required'
        NOT_REQUIRED = 'Not required'

    advance_payment_required = models.CharField(
        null=True,
        max_length=25,
        choices=advance_payment_required_options.choices,
        default=advance_payment_required_options.REQUIRED,
    )
    advance_payment_contract_providing_date = models.DateField(null=True, auto_now=False, auto_now_add=False, blank=True)
    advance_payment_paid = models.BooleanField(null=True, default=None)
    advance_payment_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
