import pandas as pd


class Load:

    def __init__(self, profile: pd.Series):
        self.profile = profile
        self.timestamp = self.profile.index[0]
        self.sampling_time = self.profile.index[1] - self.profile.index[0]

    @property
    def power(self):
        return self.profile[self.timestamp].item()

    def step(self):
        self.timestamp += self.sampling_time

    def history(self, size: pd.Timedelta) -> pd.Series:
        size = size // self.sampling_time
        from_timestamp = self.timestamp
        to_timestamp = self.timestamp + size * self.sampling_time
        return self.profile[from_timestamp:to_timestamp]
