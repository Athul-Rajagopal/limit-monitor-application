from django.db import models
from .utils import fetch_weather_data

def compare_weather_data(data, field, operator, value):
    weather_value = data.get('current').get(field)
    if operator == 'lt':
        return weather_value < value
    elif operator == 'gt':
        return weather_value > value
    elif operator == 'lte':
        return weather_value <= value
    elif operator == 'gte':
        return weather_value >= value
    elif operator == 'eq':
        return weather_value == value
    else:
        raise ValueError(f"Invalid comparison operator: {operator}")

class Limit(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=255)
    criteria = models.CharField(max_length=255)
    operator = models.CharField(max_length=3, choices=(('lt', '<'), ('gt', '>'), ('lte', '<='), ('gte', '>='), ('eq', '==')))
    comparison_value = models.FloatField()
    frequency = models.CharField(max_length=10, choices=(('day', 'Day'), ('month', 'Month'), ('year', 'Year')))
    status = models.CharField(max_length=255, default='Active')

    def is_met(self):
        weather_data = fetch_weather_data(self.location)
        if weather_data:
            field = self.criteria.split()[0]  # Extract the field from the criteria string
            return compare_weather_data(weather_data, field, self.operator, self.comparison_value)
        return False

    def save(self, *args, **kwargs):
        if self.is_met():
            self.status = 'Completed'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.location} - {self.criteria}"
