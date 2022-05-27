import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

%matplotlib notebook

df=pd.read_csv(r'C:\Users\HP\Documents\iris.csv')

df.columns=np.array(['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class'])

df.head()

df.tail()

df.describe()

df['Sepal Width'].describe()

df.dtypes

sns.heatmap(df.corr(), annot=True)

# Positive correlation
sns.lmplot(x='Petal Width', y='Petal Length', data=df)

# Negative correlation
sns.lmplot(x='Sepal Width', y='Petal Length', data=df)