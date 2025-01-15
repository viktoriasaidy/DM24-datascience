import pandas as pd
print(pd.__version__)

data = {
    "Name": ["Anna", "Björn", "Cecilia"],
    "Age": [25, 30, 27],
    "City": ["Stockholm", "Göteborg", "Malmö"]
}
df = pd.DataFrame(data)
print(df)

ages = df["Age"]
filtered_data = df[df["Age"] > 25]
print(filtered_data)