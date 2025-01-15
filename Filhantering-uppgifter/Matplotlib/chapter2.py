"""""
import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 100)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
plt.show()
"""""
"""""
import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.plot(x_vals, y2_vals, 'b', label = 'Cube')
plt.legend(loc='upper center')
plt.show()
"""""

import matplotlib.pyplot as plt
import numpy as np
import math
labels = 'Datamodellering och design', 'Att arbete i projekt', 'Data arkitektur', 'Data science'
values = [30, 20, 25, 40]
explode = (0.05, 0.05, 0.05, 0.05) 

plt.pie(values, explode=explode, labels=labels, 
autopct='%1.1f%%', shadow=True, startangle=140, colors=['pink', 'purple', 'red', 'blue'], )
plt.show()
