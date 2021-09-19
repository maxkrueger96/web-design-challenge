import pandas as pd
from urlscript import tablelinks, pokemon

#first lets make each pokemon's name a link to an online pokemon database
urls =  dict.fromkeys(pokemon.name)
htmls = dict.fromkeys(pokemon.name)
tablelinks(urls,htmls)

for n in pokemon.name:
    pokemon.replace(n,htmls[n],inplace=True)

#convert to html and save
pokemon.set_index(pokemon.pokedex_number,inplace=True)
pokemon.drop(columns="pokedex_number",inplace=True)
pokemon.to_html("urltable.html",escape=False)
