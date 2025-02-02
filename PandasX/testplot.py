import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D']
values1 = [10, 15, 20, 25]
values2 = [12, 18, 22, 28]

# Define the width of the bars and their positions
bar_width = 0.35
index = np.arange(len(categories))

# Create the plot
fig, ax = plt.subplots()

# Plot the bars
bar1 = ax.bar(index, values1, bar_width, label='Set 1', color='b')
bar2 = ax.bar(index + bar_width, values2, bar_width, label='Set 2', color='g')

# Add labels, title, and legend
ax.set_xlabel('Category')
ax.set_ylabel('Values')
ax.set_title('Paired Column Chart')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()

# Display the plot
plt.show()