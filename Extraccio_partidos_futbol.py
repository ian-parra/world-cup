from bs4 import BeautifulSoup
import requests
import pandas as pd

# data to scraper -> 1930-2022
years = [2022]


def get_matches(year):
    wep = f'https://web.archive.org/web/20221115040351/https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
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


"""# historical_data
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_historical_data2022.csv', index=False)"""

# fixture 2022
df_fixture = get_matches(2022)
df_fixture.to_csv('fifa_worldcup_fixture2022.csv', index=False)
