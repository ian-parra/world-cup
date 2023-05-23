import pandas as pd

df_historical_data = pd.read_csv('data/fifa_worldcup_historical_data2022.csv')

# Limpieza de la columna de puntaje y las columnas de equipo local/visitante
df_historical_data['score'] = df_historical_data['score'].str.replace('[^\d–]', '', regex=True)
df_historical_data['home'] = df_historical_data['home'].str.strip()
df_historical_data['away'] = df_historical_data['away'].str.strip()

# División de la columna de puntaje en goles del equipo local y visitante, y eliminación de la columna de puntaje
df_historical_data[['Goles del Local', 'Goles del Visitante']] = df_historical_data['score'].str.split('–', expand=True)
df_historical_data.drop('score', axis=1, inplace=True)

# Renombrar columnas y cambiar los tipos de datos
df_historical_data.rename(columns={'home': 'Equipo Local', 'away': 'Equipo Visitante', 'year': 'Año'}, inplace=True)
df_historical_data.dropna(subset=['Goles del Local', 'Goles del Visitante', 'Año'], inplace=True)
df_historical_data['Goles del Local'] = df_historical_data['Goles del Local'].astype(int)
df_historical_data['Goles del Visitante'] = df_historical_data['Goles del Visitante'].astype(int)
df_historical_data['Año'] = df_historical_data['Año'].astype(int)

# Crear nueva columna "Goles Totales"
df_historical_data['Goles Totales'] = df_historical_data['Goles del Local'] + df_historical_data['Goles del Visitante']

# Exportar los datos limpios
df_historical_data.to_csv('clean_fifa_worldcup_matches2022.csv', index=False)
