from cbrf.models import DailyCurrenciesRates

daily = DailyCurrenciesRates()
usd = daily.get_by_id('R01235').value
eur = daily.get_by_id('R01239').value
gbp = daily.get_by_id('R01035').value

