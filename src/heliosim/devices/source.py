import pandas as pd


class Source:

    def __init__(self, profile: pd.Series):
        self.profile = profile
