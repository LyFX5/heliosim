import numpy as np
import gymnasium as gym
import sys

sys.modules["gym"] = gym
from pymgrid import Microgrid


class DemoMicrogrid:
    def __init__(self, devices, load_profile, tariff_profile=None):
        self.devices = devices
        self.load = load_profile
        self.tariff = (
            tariff_profile
            if tariff_profile is not None
            else np.zeros_like(load_profile)
        )

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

        return {"electrolyser_power": elec_power, "h2_produced_kg": h2}
