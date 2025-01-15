import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fruits.csv")
print(df)

försäljningÖverTid = df.groupby("Date").sum("Sales")
print(försäljningÖverTid)

plt.plot(försäljningÖverTid.index, försäljningÖverTid["Sales"])
plt.title("Stapeldiagram")
plt.xlabel("Frukt")
plt.ylabel("Total försäljning")
plt.xticks(rotation=45)
plt.show()
