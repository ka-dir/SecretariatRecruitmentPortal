import uuid

from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)  # 0=EXTERNAL; 1=INTERNAL


class Status(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)  # 0=OPEN; 1=CLOSED; 2=DRAFT


class TargetGroup(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)  # 0=SECRETARIAT; 1=TEACHERS; 2=BOTH


class TermOfService(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)  # 0=PERMANENT; 1=INTERN; 2=CONTRACT


class PayType(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)  # 0=MONTHLY; 1=YEARLY;


class Advert(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    advert_no = models.CharField(max_length=20, db_index=True, unique=True)
    post_vacancy = models.CharField(max_length=100, blank=True, null=True)
    no_of_post = models.IntegerField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)
    job_description = models.TextField(blank=True, null=True)
    duties_responsibilities = models.TextField(blank=True, null=True)
    job_requirements = models.TextField(blank=True, null=True)
    pay_type = models.ForeignKey(PayType, on_delete=models.SET_NULL, blank=True, null=True)
    currency = models.CharField(max_length=10, default='Kes')
    basic_salary = models.CharField(max_length=100, blank=True, null=True)
    house_allowance = models.CharField(max_length=100, blank=True, null=True)
    commuter_allowance = models.CharField(max_length=100, blank=True, null=True)
    leave_allowance = models.CharField(max_length=100, blank=True, null=True, default='As provided in TSC Secretariat')
    medical_scheme = models.CharField(max_length=100, blank=True, null=True,
                                      default='As provided in the TSC Secretariat Medical Scheme')
    is_closed = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
    category_target_group = models.ForeignKey(TargetGroup, on_delete=models.SET_NULL, blank=True, null=True)
    term_of_service = models.ForeignKey(TermOfService, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_vacancy
