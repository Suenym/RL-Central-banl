import pandas as pd
import yaml


def load_macro_series(country_config: str):
    with open(country_config) as f:
        cfg = yaml.safe_load(f)
    data = pd.DataFrame()
    if 'series_file' in cfg:
        try:
            data = pd.read_csv(f"data/{cfg['series_file']}")
        except FileNotFoundError:
            pass
    return data
