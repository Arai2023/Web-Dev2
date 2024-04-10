from django.db import models # type: ignore

# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE) # type: ignore

    def __str__(self):
        return f'{self.name}: {self.description}. {self.salary}, {self.company}'

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }
    
    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField()
    address = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.description}. {self.city}, {self.address}'

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

