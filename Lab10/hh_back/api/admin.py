from django.contrib import admin # type: ignore
from .models import Company, Vacancy

admin.site.register(Company)
admin.site.register(Vacancy)