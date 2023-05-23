import pandas as pd

df_historical_data = pd.read_csv('data/fifa_worldcup_historical_data.csv')
df_fixture = pd.read_csv('data/fifa_worldcup_fixture.csv')

# Limpieza del fixture
df_fixture['home'] = df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()

# Limpieza de datos históricos por años
df_historical_data.drop_duplicates(inplace=True)
df_historical_data.sort_values('year', inplace=True)

# Eliminación del partido con walk over
delete_index = df_historical_data[df_historical_data['home'].str.contains('Sweden') &
                                  df_historical_data['away'].str.contains('Austria')].index

df_historical_data.drop(index=delete_index, inplace=True)

# Limpieza de la columna de puntaje y las columnas de equipo local/visitante
df_historical_data['score'] = df_historical_data['score'].str.replace('[^\d–]', '', regex=True)
df_historical_data['home'] = df_historical_data['home'].str.strip()  # Limpiar espacios en blanco: Yugoslavia
df_historical_data['away'] = df_historical_data['away'].str.strip()

# División de la columna de puntaje en goles del equipo local y visitante, y eliminación de la columna de puntaje
df_historical_data[['HomeGoals', 'AwayGoals']] = df_historical_data['score'].str.split('–', expand=True)
df_historical_data.drop('score', axis=1, inplace=True)

# Renombrar columnas y cambiar los tipos de datos
df_historical_data.rename(columns={'home': 'HomeTeam', 'away': 'AwayTeam', 'year': 'Year'}, inplace=True)
df_historical_data.dropna(subset=['HomeGoals', 'AwayGoals', 'Year'], inplace=True)
df_historical_data['HomeGoals'] = df_historical_data['HomeGoals'].astype(int)
df_historical_data['AwayGoals'] = df_historical_data['AwayGoals'].astype(int)
df_historical_data['Year'] = df_historical_data['Year'].astype(int)

# Crear nueva columna "TotalGoals"
df_historical_data['TotalGoals'] = df_historical_data['HomeGoals'] + df_historical_data['AwayGoals']

# Exportar los datos limpios
df_historical_data.to_csv('clean_fifa_worldcup_matches.csv', index=False)
df_fixture.to_csv('clean_fifa_worldcup_fixture.csv', index=False)

