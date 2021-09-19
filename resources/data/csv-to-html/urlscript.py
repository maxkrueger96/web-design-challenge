import pandas as pd
import requests

pokemon = pd.read_csv(open("resources/data/pokemon.csv"))

#get rid of duplicate pokedex numbers
pokemon.drop_duplicates(subset="pokedex_number",inplace=True,ignore_index=True)

#get rid of type effectiveness columns
types = pokemon.typing.drop_duplicates()
monotypes = []
for t in types:
    if '~' not in t:
        monotypes.append(t)
effectives = [f'{t.lower()}_attack_effectiveness' for t in monotypes if t != 'Flying']
effectives.append('fly_attack_effectiveness')
pokemon.drop(columns=effectives,inplace=True)

pokedex = pokemon[["pokedex_number","name"]].copy()

def urlshtmlssm(dict1,dict2):
    for n in pokedex.name[pokedex.pokedex_number<10]:
        no = f"00{pokedex.pokedex_number[pokedex.name==n].values[0]}"
        urlist = [f"https://www.serebii.net/pokedex-swsh/{no}.shtml",f"https://www.serebii.net/pokedex-sm/{no}.shtml"]
        while dict1[n]==None:
            for i in range(len(urlist)):
                req = requests.get(urlist[i])
                reqst = req.status_code
                if reqst == 200:
                    dict1[n]=urlist[i]
                    break
                else:
                    continue
            break
        if dict1[n]==None:
            dict1[n] = f"https://www.serebii.net/search.shtml?cx=018410473690156091934%3A6gahkiyodbi&cof=FORID%3A11&q={n}&sa=Search"
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
        else:
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
    return

def urlshtmlsmed(dict1,dict2):
    for n in pokedex.name[pokedex.pokedex_number>=10].loc[pokedex.pokedex_number<100]:
        no = f"0{pokedex.pokedex_number[pokedex.name==n].values[0]}"
        urlist = [f"https://www.serebii.net/pokedex-swsh/{no}.shtml",f"https://www.serebii.net/pokedex-sm/{no}.shtml"]
        while dict1[n]==None:
            for i in range(len(urlist)):
                req = requests.get(urlist[i])
                reqst = req.status_code
                if reqst == 200:
                    dict1[n]=urlist[i]
                    break
                else:
                    continue
            break
        if dict1[n]==None:
            dict1[n] = f"https://www.serebii.net/search.shtml?cx=018410473690156091934%3A6gahkiyodbi&cof=FORID%3A11&q={n}&sa=Search"
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
        else:
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
    return
                        
def urlshtml(dict1,dict2):
    for n in pokedex.name:
        no = pokedex.pokedex_number[pokedex.name==n].values[0]
        urlist = [f"https://www.serebii.net/pokedex-swsh/{no}.shtml",f"https://www.serebii.net/pokedex-sm/{no}.shtml"]
        while dict1[n]==None:
            for i in range(len(urlist)):
                req = requests.get(urlist[i])
                reqst = req.status_code
                if reqst == 200:
                    dict1[n]=urlist[i]
                    break
                else:
                    continue
            break
        if dict1[n]==None:
            dict1[n] = f"https://www.serebii.net/search.shtml?cx=018410473690156091934%3A6gahkiyodbi&cof=FORID%3A11&q={n}&sa=Search"
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
        else:
            dict2[n] = f"<a class=table-link href={dict1[n]}>{n}</a>"
    return

def tablelinks(dict1,dict2):
    urlshtmlssm(dict1,dict2)
    urlshtmlsmed(dict1,dict2)
    urlshtml(dict1,dict2)
    return