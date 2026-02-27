from abc import abstractmethod
from pandas import Timedelta
from typing import Dict, Any


class Device:

    @abstractmethod
    def state(self) -> Dict: ...

    @abstractmethod
    def step(self, control: Any, dt: Timedelta) -> None: ...
