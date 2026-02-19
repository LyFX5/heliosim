from abc import ABC, abstractmethod
from typing import Dict, List


class EnergyFlowSchema(ABC): ...


class SchemaA(EnergyFlowSchema):

    @classmethod
    def step(
        cls,
        source,
        load,
        battery,
        electrolysers,
        fuel_cell,
        utility_grid,
    ):
        remaining_power = source.power
        if load is not None:
            remaining_power -= load.power
        for elec in electrolysers:
            remaining_power -= elec.power
        if battery is not None:
            battery.step(remaining_power, source.sampling_time)
            remaining_power -= battery.charge_power
            remaining_power += battery.discharge_power
        if utility_grid is not None:
            utility_grid.step(remaining_power)
            remaining_power -= utility_grid.export_power
            remaining_power += utility_grid.import_power
        return remaining_power
