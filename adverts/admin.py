from django.contrib import admin
from .models import Category, Status, TargetGroup, TermOfService, PayType, Advert
# Register your models here.

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(TargetGroup)
admin.site.register(TermOfService)
admin.site.register(PayType)
admin.site.register(Advert)