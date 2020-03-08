import pandas as pd
from decimal import Decimal

data = pd.read_csv("nba.games.stats.csv")
print(data.head())

matches = data.shape[0]
team = "LAC"
wins = len(data.query(f'Team=="{team}" & Home=="Home" & WINorLOSS =="W"'))
losses = len(data.query(f'Team=="{team}" & Home=="Home" & WINorLOSS =="L"'))
homegames = len(data.query(f'Team=="{team}" & Home=="Home"'))
print(homegames)

homewinrate = (wins / homegames) * 100
homewinrate = round(homewinrate,2)
#(float(wins) / (homegames)) * 100

#print("Total number of matches: " + str(matches))
print(f"Number of matches won by {team} when at Home: {wins}")
print(f"Win rate of {team} when at Home: {homewinrate}%")
