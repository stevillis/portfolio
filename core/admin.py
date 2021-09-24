from django.contrib import admin

from core.models import Academy


@admin.register(Academy)
class AcademyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Academy._meta.get_fields()]
