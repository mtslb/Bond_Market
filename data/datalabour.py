from fredapi import Fred
from utils.api import FRED_API_KEY
from utils.constants import date_start

fred = Fred(api_key=FRED_API_KEY)

unemployment = fred.get_series("UNRATE", observation_start=date_start)
nfp = fred.get_series("PAYEMS", observation_start=date_start)
initial_claims = fred.get_series("ICSA", observation_start=date_start)
participation = fred.get_series("CIVPART", observation_start=date_start)