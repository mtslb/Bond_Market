from fredapi import Fred

import pandas as pd
from utils.api import FRED_API_KEY
from utils.constants import date_start

fred = Fred(api_key=FRED_API_KEY)

fed_rate = fred.get_series("FEDFUNDS", observation_start=date_start)
fed_balance_sheet = fred.get_series("WALCL", observation_start=date_start)
m2 = fred.get_series("M2SL", observation_start=date_start)