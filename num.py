
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Banking.csv")
print(df)








numerical_col=['BRId', 'GenderId']
plt.figure(figsize=(30,20))
for i, col in enumerate(numerical_col):
    plt.subplot(2,1,i+1)
    sns.histplot(data=df,x=col,kde=True)
    plt.title(col)
    
plt.show()
