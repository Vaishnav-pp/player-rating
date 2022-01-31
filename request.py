import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'role':0, ' Goals Conceded':1, ' Minutes played':90, ' Punches':0, 'Saves':0,
       'Throws':2, 'Passes':30, 'Accurate Passes':25, 'Key Passes':3, 'goals':2, 'assists':1,
       'chances_created':4, 'total_shots':5, 'shot_on_target':4, 'crosses':2,
       'long_balls':0, 'touches':40, 'aerials_won':2, 'aerials_lost':2, 'clearances':4,
       'dispossessed':5, 'dribbles_attempted':10, 'dribbles_succeeded':8, 'duels_won':3,
       'duels_lost':2, 'fouls':0, 'interceptions':1, 'recoveries':1,
       'tackles_attempted':3, 'tackles_succeeded':2, 'was_fouled':2, 'is_a_sub':0,
       'was_subbed':0, 'yellow_card':1, 'red_card':0})

print(r.json())