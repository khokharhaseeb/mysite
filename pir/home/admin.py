from django.contrib import admin
from .models import contact_message,medical_billing,dental_billing,credentialing
# Register your models here.
@admin.register(contact_message)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(medical_billing)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(dental_billing)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(credentialing)
class AuthorAdmin(admin.ModelAdmin):
    pass