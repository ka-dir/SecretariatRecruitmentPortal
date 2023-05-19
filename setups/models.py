from django.db import models


# Create your models here.

class Gender(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title


class Salutation(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title


class Nationality(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Nationality'
        verbose_name_plural = 'Nationalities'

    def __str__(self):
        return self.title


class County(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.title


class Constituency(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Constituency'
        verbose_name_plural = 'Constituencies'

    def __str__(self):
        return self.title


class Subounty(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Subounty'
        verbose_name_plural = 'Subounties'

    def __str__(self):
        return self.title


class MaritalStatus(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'MaritalStatus'
        verbose_name_plural = 'MaritalStatus'

    def __str__(self):
        return self.title


class Disability(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    class Meta:
        verbose_name = 'Disability'
        verbose_name_plural = 'Disabilities'

    def __str__(self):
        return self.title


class Relationship(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title
