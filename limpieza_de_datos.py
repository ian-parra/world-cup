import pandas as pd

df_historical_data = pd.read_csv('data/fifa_worldcup_historical_data.csv')
df_fixture = pd.read_csv('data/fifa_worldcup_fixture2022.csv')

# limpiando el fixture
df_fixture['home'] = df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()

# Limpieza de historical date por años
df_historical_data.drop_duplicates(inplace=True)
df_historical_data.sort_values('year', inplace=True)

# eliminacion de partido por 3 a 0 arbitrario walkover
eliminar_index = df_historical_data[df_historical_data['home'].str.contains('Sweden') &
                                    df_historical_data['away'].str.contains('Austria')].index

df_historical_data.drop(index=eliminar_index, inplace=True)

# columnas local/visitante limpiando el score cuando los partidos llega a penales 
df_historical_data['score'] = df_historical_data['score'].str.replace('[^\d–]', '', regex=True)
df_historical_data['home'] = df_historical_data['home'].str.strip() #espacios en blanco limpios: Yugoslavia
df_historical_data['away'] = df_historical_data['away'].str.strip(
