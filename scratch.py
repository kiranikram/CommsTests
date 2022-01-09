import random 
import scipy.stats as stats

seasons = [1,2,3]

forecast_1 = random.choices(seasons,k=8)
forecast_2 = random.choices(seasons,k=8)
forecast_3 = random.choices(seasons,k=8)


season = lambda x: stats.mode(x)[0][0]
print(season(forecast_1))
print(season(forecast_2))
print(season(forecast_3))