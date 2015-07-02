from django.contrib import admin

from .models import Grant, AccessToken, RefreshToken, get_application_model

class RawIDAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
