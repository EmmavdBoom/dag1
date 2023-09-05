print('Start van de api applicatie')

import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print (paginaresults)

feitjes = paginaresults.json() #lees de pagina die we hebben gedownload en zet om in data die we kunnen weergeven.
print("Feitje is " + feitjes["data"][0]["fact"]) #0 is het aller eerste feitje. Via json formatter kun je zien of data ook "data" heet.


