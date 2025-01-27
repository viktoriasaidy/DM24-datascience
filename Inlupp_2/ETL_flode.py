# Läsa in CSV filen
import pandas as pd

file_path = "C:\\Users\\vikto\\Downloads\\Valdeltagande_förstagångsväljare_2004_2014 (1).csv"

df = pd.read_csv(file_path)
print(df)
