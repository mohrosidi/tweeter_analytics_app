from utils.eda import perform_eda

class EDAAgent:
    def __init__(self):
        """EDA Agent tidak membutuhkan API Key."""
        pass

    def perform_eda(self, df):
        """Melakukan Exploratory Data Analysis (EDA) pada DataFrame tweet."""
        return perform_eda(df)
