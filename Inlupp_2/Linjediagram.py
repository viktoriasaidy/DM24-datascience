import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\Inlupp_2\\andel-matavfall-som-behandlas-biologiskt.csv"

df = pd.read_csv(file_path, sep=";")
print(df)

matavfall_per_år = df.groupby('År')['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
print(matavfall_per_år)

plt.figure(figsize=(10, 6))
plt.plot(matavfall_per_år['År'], matavfall_per_år['Andel matavfall som behandlas biologiskt, %'])

# Linjediagram
plt.xlabel('År')
plt.ylabel('Andel matavfall som behandlas biologiskt, %')
plt.title('Andel matavfall behandlat biologiskt per år')
plt.show()
