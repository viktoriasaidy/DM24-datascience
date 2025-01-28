import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\Inlupp_2\\andel-matavfall-som-behandlas-biologiskt.csv"

df = pd.read_csv(file_path, sep=";")
print(df)

matavfall_genomsnitt = df.groupby('Kommun/ förbund')['Andel matavfall som behandlas biologiskt, %'].mean().reset_index()
matavfall_genomsnitt = matavfall_genomsnitt.sort_values(by='Andel matavfall som behandlas biologiskt, %', ascending=False)
print(matavfall_genomsnitt)

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(matavfall_genomsnitt['Andel matavfall som behandlas biologiskt, %'], bins=10, edgecolor='black')
plt.xlabel('Andel matavfall som behandlas biologiskt, %')
plt.ylabel('Antal kommuner')
plt.title('Fördelning av andel matavfall behandlat biologiskt per kommun')
plt.show()