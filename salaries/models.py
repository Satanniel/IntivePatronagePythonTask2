from django.db import models


class Employee(models.Model):
    worked_years = models.FloatField('Worked years')
    salary_brutto = models.FloatField('Salary brutto')
