import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

file_path = "C:\\Users\\vikto\\OneDrive\\Dokument\\DATA MANAGER 2024\\Data science\\Inlupp_2\\andel-matavfall-som-behandlas-biologiskt.csv"

df = pd.read_csv(file_path, sep=";")
print(df)

# Scatter diagram
plt.figure(figsize=(10, 6))
plt.scatter(df['År'], df['Andel matavfall som behandlas biologiskt, %'], color='orange')  
plt.xlabel('År')
plt.ylabel('Andel matavfall som behandlas biologiskt, %')
plt.title('Andel matavfall som behandlas biologiskt per år')
plt.show()