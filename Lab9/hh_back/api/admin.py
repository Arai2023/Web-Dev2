from django.contrib import admin # type: ignore
from models import Company, Vacancy

# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'description', 'salary', 'company')
    search_fields = ('name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description','city', 'address')