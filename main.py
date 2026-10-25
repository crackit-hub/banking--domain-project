import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Banking.csv")
print(df)

print(df.shape)

print(df.head(5))

print(df.info())

# describtive statictics
print(df.describe())

pd.set_option('display.max_columns',None)

print(df.columns .to_list())


# selecting and count values
categorical_cols = ['BRId', 'GenderId']

for col in categorical_cols:
    print(f"\nValue counts for '{col}':")
    print(df[col].value_counts())

# graph

categorical_cols = ['BRId', 'GenderId','Age','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']

for i, predictor in enumerate(categorical_cols):
    plt.figure(i)
    sns.countplot(data=df, x=predictor)
    plt.title(f'Distribution of {predictor}')
    plt.show()



categorical_cols = ['BRId', 'GenderId','Age','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']

for i, predictor in enumerate(categorical_cols):
    plt.figure(i)
    sns.boxplot(data=df, x=predictor)
    plt.title(f'Distribution of {predictor}')
    plt.show()


#numerical analysis

numerical_col=['BRId', 'GenderId','Age']
plt.figure(figsize=(30,20))
for i, col in enumerate(numerical_col):
    plt.subplot(2,1,i+1)
    sns.histplot(df([col],kde=True))
    plt.title(col)
    
plt.show()



