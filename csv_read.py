print('Start met csv uitlees applicatie')

import pandas

df = pandas.read_csv('pokemon.csv') # df = DataFrame
print(df["Name"]) #dit is een array

# Pandas - Library - Dependency - Packages: namen/labels voor iemand anders zijn codes waar je gebruik van maakt

for r,rij in df.iterrows():
    print(rij["Name"])
    print("De naam van de pokemons is"+ rij ["Name"] )