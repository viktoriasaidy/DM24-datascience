# import pandas as pd
# import matplotlib.pyplot as plt

# file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\GruppArbete\\processed_data_befolkningsförändringar.csv"

# df = pd.read_csv(file_path)
# print(df)
# df.sort_values(by='år', ascending=True, inplace=True)

# plt.figure(figsize=(10, 6))
# plt.plot(df['år'], df['invandringar'], label='Invandring', marker='o')
# plt.plot(df['år'], df['utvandringar'], label='Utvandring', marker='o')

# plt.title('Invandring vs Utvandring per år', fontsize=16)
# plt.xlabel('År', fontsize=12)
# plt.ylabel('Antal personer', fontsize=12)
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Läs in data
file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\GruppArbete\\processed_data_befolkningsförändringar.csv"
data = pd.read_csv(file_path)

# Kontrollera data
print(data.head())

# Säkerställ att kolumner är numeriska
data['år'] = pd.to_numeric(data['år'], errors='coerce')
data['tillväxttakt'] = pd.to_numeric(data['tillväxttakt'], errors='coerce')

# Ta bort rader med saknade värden
data = data.dropna(subset=['år', 'tillväxttakt'])

# Förbered data för regression
X = data[['år']]  # Oberoende variabel
y = data['tillväxttakt']  # Beroende variabel

# Skapa och träna modellen
model = LinearRegression()
model.fit(X, y)

# Generera framtida år
future_years = pd.DataFrame({'år': range(data['år'].max() + 1, data['år'].max() + 11)})

# Gör förutsägelser
future_predictions = model.predict(future_years)

# Visualisera historiska och förutsagda värden
plt.figure(figsize=(10, 6))
plt.scatter(data['år'], data['tillväxttakt'], color='blue', label='Historiska data')
plt.plot(data['år'], model.predict(X), color='green', label='Regression (trend)')
plt.plot(future_years, future_predictions, color='red', linestyle='--', label='Förutsägelser')
plt.xlabel('år', fontsize=12)
plt.ylabel('tillväxttakt (%)', fontsize=12)
plt.title('Förutsägelse av befolkningstillväxt', fontsize=16)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()