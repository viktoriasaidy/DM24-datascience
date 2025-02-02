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
# df.to_csv("rensadData.csv", index=False)

# Totalt matavfall per år
matavfall_per_år = df.groupby('År')['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
print(matavfall_per_år)
# matavfall_per_år.to_csv("matavfall_per_år.csv", index=False)

# Vilket år presterade enskilda kommuner högst i andel matavfall behandlat biologiskt?
kommun_med_högst_matavfall = df.groupby(['Kommun/ förbund', 'År'])['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
bäst_presterande_år_per_kommun = kommun_med_högst_matavfall.loc[kommun_med_högst_matavfall.groupby('Kommun/ förbund')['Andel matavfall som behandlas biologiskt, %'].idxmax()]
print(bäst_presterande_år_per_kommun)
# bäst_presterande_år_per_kommun.to_csv("kommun_med_högst_matavfall.csv", index=False)

# År med sämst prestering 
kommun_med_lägst_matavfall = df.groupby(['Kommun/ förbund', 'År'])['Andel matavfall som behandlas biologiskt, %'].sum().reset_index()
sämst_presterande_år_per_kommun = kommun_med_lägst_matavfall.loc[kommun_med_lägst_matavfall.groupby('Kommun/ förbund')['Andel matavfall som behandlas biologiskt, %'].idxmin()]
print(sämst_presterande_år_per_kommun)
# sämst_presterande_år_per_kommun.to_csv("sämst_presterande_år_per_kommun.csv", index=False)

# Hur presterar kommunerna i genomsnitt?
matavfall_genomsnitt = df.groupby('Kommun/ förbund')['Andel matavfall som behandlas biologiskt, %'].mean().reset_index()
matavfall_genomsnitt = matavfall_genomsnitt.sort_values(by='Andel matavfall som behandlas biologiskt, %', ascending=False)
print(matavfall_genomsnitt)
# matavfall_genomsnitt.to_csv("matavfall_genomsnitt.csv", index=False)

# Skapa en ny kolumn 'Län' som innehåller länets namn för varje kommun.
kommun_till_län = {
    "Nordmaling": "Västerbottens län",
    "Bjurholm": "Västerbottens län",
    "Umeå": "Västerbottens län",
    "Robertsfors": "Västerbottens län",
    "Vindeln": "Västerbottens län",
    "Vännäs": "Västerbottens län"
}
df["Län"] = df["Kommun/ förbund"].map(kommun_till_län)
print(kommun_till_län)
# df.to_csv("kommun_till_län.csv", index=False)

#Exportera till excel
matavfallGenomsnitt = r"C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\matavfallGenomsnitt.xlsx"
matavfall_genomsnitt.to_excel(matavfallGenomsnitt, index=False)