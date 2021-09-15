import pandas as pd

path = './resources/data/pokemon.csv'
pokemon = pd.read_csv(path)

#get rid of gigamax and mega forms
gmax_names = [p for p in pokemon.name if 'Gmax' in p or 'Mega' in p and p != 'Meganium']
gmax_megas = pd.Series(gmax_names,name='name')
gmax_megas = pokemon.merge(gmax_megas)
for p in pokemon.name:
    if 'Gmax' in p or 'Mega' in p:
        if p == 'Meganium':
            pass
        else:
            pokemon.drop(pokemon.loc[pokemon.name == p].index,axis=0,inplace=True)

#get rid of type effectiveness columns
types = pokemon.typing.drop_duplicates()
monotypes = []
for t in types:
    if '~' not in t:
        monotypes.append(t)
effectives = [f'{t.lower()}_attack_effectiveness' for t in monotypes if t != 'Flying']
effectives.append('fly_attack_effectiveness')
pokemon.drop(columns=effectives,inplace=True)

#convert to html and save
pokemon.to_html('data.html')
