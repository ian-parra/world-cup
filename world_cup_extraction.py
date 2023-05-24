import pandas as pd
from string import ascii_uppercase as abecedario
import pickle

todas_Tablas = pd.read_html(
    'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki''/2022_FIFA_World_Cup')

dict_table = {}
for letter, i in zip(abecedario, range(12, 68, 7)):
    df = todas_Tablas[i]
    df.rename(columns={df.columns[1]: 'Team'}, inplace=True)
    df.pop('Qualification')
    dict_table[f'Group {letter}'] = df

with open('data/dict_table', 'wb') as output:
    pickle.dump(dict_table, output)
