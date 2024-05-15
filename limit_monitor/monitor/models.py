from django.db import models
from .utils import fetch_weather_data

# Create your models here.

def compare_weather_data(data, criteria):
    # Parse criteria string (e.g., "temperature > 30")
    field, operator, value = criteria.split()
    value = float(value)  # Assuming value is a number

    # Extract relevant data based on field name
    weather_value = data.get('current').get(field)  # Example: data['current'].get('temp_c') for temperature in Celsius

    # Evaluate comparison
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
    criteria = models.CharField(max_length=255)  # Store criteria details (e.g., temperature > 30)
    operator = models.CharField(max_length=3, choices=(('lt', '<'), ('gt', '>'), ('lte', '<='), ('gte', '>='), ('eq', '==')))
    comparison_value = models.FloatField()  # Or other data type based on criteria
    frequency = models.CharField(max_length=10, choices=(('day', 'Day'), ('month', 'Month'), ('year', 'Year')))
    status = models.CharField(max_length=255, default='Active')  # Can be 'Completed' or other status values


    def is_met(self):
        weather_data = fetch_weather_data(self.location)  # Replace with actual function to fetch data (likely in utils.py)
        if weather_data:
            return compare_weather_data(weather_data, self.criteria)
        return False  # Handle cases where weather data cannot be fetched

    def __str__(self):
        return f"{self.location} - {self.criteria}"  # Customize representation