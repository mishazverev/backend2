from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


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
    measurement_date = models.DateField(null=True, default=timezone.now, auto_now=False, auto_now_add=False)
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
    brands = models.CharField(max_length=100, null=True, blank=True)
    brands_id = models.ManyToManyField(Brand)

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
    id = models.BigAutoField(primary_key=True)
    premise_id = models.ManyToManyField(PremiseMain)
    tenant_contractor_id = models.ForeignKey(TenantContractor, on_delete=DO_NOTHING, null=True, default='')
    rent_contract_number = models.CharField(max_length=50, null=True, unique=True)
    contracted_area = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=DO_NOTHING, null=True)
    contract_signing_date = models.DateField(default=timezone.now, auto_now=False, auto_now_add=False, null=True)
    rent_start_date = models.DateField(default=timezone.now, auto_now=False, auto_now_add=False)
    stop_billing_date = models.DateField(default=timezone.now, auto_now=False, auto_now_add=False, null=True)
    premise_return_date = models.DateField(default=timezone.now, auto_now=False, auto_now_add=False, null=True)
    duration_years = models.IntegerField(null=True)
    duration_months = models.IntegerField(null=True)
    duration_days = models.IntegerField(null=True)
    rent_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    service_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    marketing_fee_per_sqm = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)
    turnover_fee = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)
    CA_utilities_compensation_fee_fixed = models.DecimalField(null=True, max_digits=10, decimal_places=2, default=0)

    class utilities_compensation_types(models.TextChoices):
        BY_COUNTERS = 'By counters'
        FIXED = 'Fixed'
        NONE = 'None'

    utilities_compensation_type = models.CharField(
        null=True,
        max_length=20,
        choices=utilities_compensation_types.choices,
        default=utilities_compensation_types.BY_COUNTERS, )

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

    class rent_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'

    rent_fee_indexation_type = models.CharField(
        null=True,
        max_length=10,
        choices=rent_fee_indexation_types.choices,
        default=rent_fee_indexation_types.CPI, )

    class service_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'

    service_fee_indexation_type = models.CharField(
        null=True,
        max_length=10,
        choices=service_fee_indexation_types.choices,
        default=service_fee_indexation_types.FIXED, )

    class marketing_fee_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'

    marketing_fee_indexation_type = models.CharField(
        null=True,
        max_length=10,
        choices=marketing_fee_indexation_types.choices,
        default=marketing_fee_indexation_types.FIXED, )

    class utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'

    utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=10,
        choices=utilities_compensation_fixed_indexation_types.choices,
        default=utilities_compensation_fixed_indexation_types.FIXED, )

    class CA_utilities_compensation_fixed_indexation_types(models.TextChoices):
        FIXED = 'Fixed'
        CPI = 'CPI'
        REVISABLE = 'Revisable'

    CA_utilities_compensation_fixed_indexation_type = models.CharField(
        null=True,
        max_length=10,
        choices=CA_utilities_compensation_fixed_indexation_types.choices,
        default=CA_utilities_compensation_fixed_indexation_types.FIXED, )

    rent_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)
    service_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)
    marketing_fee_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2, default=0)
    utilities_compensation_fixed_indexation_fixed = models.DecimalField(null=True, max_digits=4, decimal_places=2,
                                                                        default=0)
    CA_utilities_compensation_fee_fixed_indexation_type_fixed = models.DecimalField(null=True, max_digits=4,
                                                                                    decimal_places=2,
                                                                                    default=0)

    act_of_transfer_signed = models.BooleanField(default=False)
    act_of_transfer_date = models.DateField(null=True, default=timezone.now, auto_now=False, auto_now_add=False)
    rent_fee_advance_payment_day = models.IntegerField(null=True, default=10)
    service_fee_advance_payment_day = models.IntegerField(null=True, default=10)
    marketing_fee_advance_payment_day = models.IntegerField(null=True, default=10)
    CA_utilities_compensation_fee_fixed_payment_day = models.IntegerField(null=True, default=10)
    utilities_compensation_fixed_payment_day = models.IntegerField(null=True, default=10)

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
    guarantee_deposit_number_of_months = models.PositiveBigIntegerField(null=True)
    guarantee_deposit_provided = models.BooleanField(default=False)
    guarantee_bank_guarantee_expiration_date = models.DateField(null=True, default=timezone.now, auto_now=False,
                                                                auto_now_add=False)

    advance_payment_required = models.BooleanField(null=True, default=None)
    advance_payment_paid = models.BooleanField(null=True, default=None)
    advance_payment_amount = models.DecimalField(null=True, max_digits=20, decimal_places=2)

    insurance_required = models.BooleanField(null=True, default=None)
    insurance_provided = models.BooleanField(null=True, default=None)
    insurance_expiration_date = models.DateField(null=True, default=timezone.now, auto_now=False, auto_now_add=False)

    last_updated = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    user_updated = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
