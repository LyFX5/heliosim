class Electrolyser:
    def __init__(self, min_power_kW, max_power_kW, efficiency_kg_per_kWh):
        self.min_p = min_power_kW
        self.max_p = max_power_kW
        self.eff = efficiency_kg_per_kWh
