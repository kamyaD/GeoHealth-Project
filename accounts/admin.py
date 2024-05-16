from django.contrib import admin
from accounts.models import AccountsData

# Register your models here.
@admin.register(AccountsData)
class AccountsDataAdmin(admin.ModelAdmin):
    # model = AccountsData
    list_display = ("name", "file", "uploaded_at","updated_by")


