import pandas as pd

path = './resources/data/pokemon.csv'
pokefile = pd.read_csv(path)
pokefile.to_html('./resources/data/csv-to-html/pokemon.html')
