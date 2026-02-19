import numpy as np


class SolarIrradiance:
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude

    def generate(self, time_index):
        # Simplified clear-sky model + noise
        hour = time_index.hour
        day_of_year = time_index.dayofyear
        # Basic sinusoidal approximation
        ghi = np.maximum(0, 800 * np.sin(np.pi * (hour - 6) / 12))
        ghi += np.random.normal(0, 50, len(ghi))
        return ghi
