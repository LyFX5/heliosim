class PVPower:
    def __init__(self, pv_capacity_kW):
        self.capacity = pv_capacity_kW

    def power_from_irradiance(self, ghi):
        return self.capacity * (ghi / 1000.0)  # simple scaling
