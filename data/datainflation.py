from fredapi import Fred
from utils.api import FRED_API_KEY
from utils.constants import date_start

fred = Fred(api_key=FRED_API_KEY)

inflation = fred.get_series("CPIAUCSL", observation_start=date_start)
core_cpi = fred.get_series("CPILFESL", observation_start=date_start)
pce = fred.get_series("PCEPI", observation_start=date_start)
core_pce = fred.get_series("PCEPILFE", observation_start=date_start)
breakeven_10y = fred.get_series("T10YIE", observation_start=date_start)