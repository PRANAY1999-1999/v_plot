import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/home/deserteagle/workplaceself/project/vplot/vplot2.tsv", sep="\t", names=["x","y","frequency"]) 

plt.figure(figsize=(10, 6))

scatter=plt.scatter(data["x"],data["y"], c=data["frequency"], facecolor="blues")

plt.colorbar(scatter, label="frequency")

plt.xlabel('column1')
plt.ylabel('column2')
plt.title('Scatter Plot by frequency')
plt.grid()



plt.show()


