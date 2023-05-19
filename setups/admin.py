from django.contrib import admin
from .models import Gender, Salutation, Nationality, County, Constituency, Subounty, MaritalStatus, Disability, \
    Relationship

# Register your models here.
admin.site.register(Gender)
admin.site.register(Salutation)
admin.site.register(Nationality)
admin.site.register(County)
admin.site.register(Constituency)
admin.site.register(Subounty)
admin.site.register(MaritalStatus)
admin.site.register(Disability)
admin.site.register(Relationship)
