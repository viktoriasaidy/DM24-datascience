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

# # Skapa ny kolumn baserat på beräkningar eller villkor.
# df["Total röster"] = df[""] + df["2010"] + df["2006"]
# print(df)

# print(df.columns)
