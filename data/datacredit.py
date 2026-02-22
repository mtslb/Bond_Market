from fredapi import Fred
import pandas as pd
from utils.api import FRED_API_KEY
from utils.constants import date_start


fred = Fred(api_key=FRED_API_KEY)


hy_spread = fred.get_series("BAMLH0A0HYM2", observation_start=date_start)
ig_spread = fred.get_series("BAMLC0A0CM", observation_start=date_start)
nfci = fred.get_series("NFCI", observation_start=date_start)
vix = fred.get_series("VIXCLS", observation_start=date_start)