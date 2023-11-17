from django.contrib import admin
from .models import Universities, Students

class UniversitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'shortName', 'year')
admin.site.register(Universities, UniversitiesAdmin)

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName','birthDate', 'university', 'admissionYear')
admin.site.register(Students, StudentsAdmin)