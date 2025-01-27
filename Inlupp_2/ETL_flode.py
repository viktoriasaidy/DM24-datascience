# Läsa in CSV filen
import pandas as pd

file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\Inlupp_2\\andel-matavfall-som-behandlas-biologiskt.csv"

df = pd.read_csv(file_path, sep=";")
print(df)

# Hantera saknade värden
# Se ifall det finns saknade värden
print(df.isnull().values.any()) # Output: True

# Radera rader med saknade värden
print("drop")
df = df.dropna()
print(df)

# Totalt matavfall per år (Se word dokument för analys)
matavfall_per_år = df.groupby('År')['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
print(matavfall_per_år)

# Vilket år presterade enskilda kommuner högst i andel matavfall behandlat biologiskt? (Se word dokument för analys)
kommun_med_högst_matavfall = df.groupby(['Kommun/ förbund', 'År'])['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
bäst_presterande_år_per_kommun = kommun_med_högst_matavfall.loc[kommun_med_högst_matavfall.groupby('Kommun/ förbund')['Andel matavfall som behandlas biologiskt, %'].idxmax()]
print(bäst_presterande_år_per_kommun)

