from django.contrib import admin
from .models import UserModel, UserCardModel, TransferModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserCardModel)
admin.site.register(TransferModel)
