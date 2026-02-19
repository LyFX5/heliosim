class Battery:
    def __init__(self, capacity_kWh, max_charge_kW, soc_init=0.5):
        self.capacity = capacity_kWh
        self.max_charge = max_charge_kW
        self.soc = soc_init
