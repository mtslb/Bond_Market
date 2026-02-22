from fredapi import Fred
import pandas as pd
from utils.api import FRED_API_KEY
from utils.constants import date_start

fred = Fred(api_key=FRED_API_KEY)

gdp = fred.get_series("GDPC1", observation_start=date_start)   # Real GDP
industrial_prod = fred.get_series("INDPRO", observation_start=date_start)
retail_sales = fred.get_series("RSAFS", observation_start=date_start)
ism_manu = fred.get_series("NAPM", observation_start=date_start)