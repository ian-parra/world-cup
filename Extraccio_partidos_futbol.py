from bs4 import BeautifulSoup
import requests
import pandas as pd

years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]


def get_matches(year):
    wep = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(wep)

    content = response.text  # print(response.text) observación de contenido

    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')  # almaceno los partidos de futbol

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'Local': home, 'Marcador': score, 'visitante': away}
    df_football = pd.DataFrame(dict_football)

    df_football['year'] = year  # print(df_football)
    return df_football


fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index=False)





