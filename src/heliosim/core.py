import numpy as np
import pandas as pd

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

class PVPower:
    def __init__(self, pv_capacity_kW):
        self.capacity = pv_capacity_kW
    
    def power_from_irradiance(self, ghi):
        return self.capacity * (ghi / 1000.0)  # simple scaling

class Electrolyser:
    def __init__(self, min_power_kW, max_power_kW, efficiency_kg_per_kWh):
        self.min_p = min_power_kW
        self.max_p = max_power_kW
        self.eff = efficiency_kg_per_kWh

class Battery:
    def __init__(self, capacity_kWh, max_charge_kW, soc_init=0.5):
        self.capacity = capacity_kWh
        self.max_charge = max_charge_kW
        self.soc = soc_init

class Grid:
    def __init__(self, max_export_kW, max_import_kW):
        self.max_export = max_export_kW
        self.max_import = max_import_kW

class Microgrid:
    def __init__(self, devices, load_profile, tariff_profile=None):
        self.devices = devices
        self.load = load_profile
        self.tariff = tariff_profile if tariff_profile is not None else np.zeros_like(load_profile)
    
    def simulate(self, strategy="passive", horizon_hours=24, h2_target_kg=None):
        n = horizon_hours
        pv = self.devices["pv"]["power_profile"][:n]
        load = self.load[:n]
        
        if strategy == "passive":
            # Surplus → electrolyser
            surplus = np.maximum(0, pv - load)
            elec_power = np.clip(surplus, 0, 100)  # cap at 100 kW
        elif strategy == "active":
            # Simple: use grid when cheap to hit target
            elec_power = np.full(n, 50.0)  # placeholder
        
        h2 = elec_power * 0.02  # kg
        
        return {
            "electrolyser_power": elec_power,
            "h2_produced_kg": h2
        }
