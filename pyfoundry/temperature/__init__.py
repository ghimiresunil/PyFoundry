"""Temperature conversion utilities and classes."""

from pyfoundry.temperature.advanced import TemperatureConverter
from pyfoundry.temperature.converter import celsius_to_fahrenheit, fahrenheit_to_celsius
from pyfoundry.temperature.faulty import FaultyTemperatureConverter

__all__ = [
    "TemperatureConverter",
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "FaultyTemperatureConverter",
]
