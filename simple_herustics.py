import pandas
import numpy

pridictions={}

df = pandas.read_csv("train.csv")

df0 = df['PassengerId']
df1 = df['PassengerId'].shift(1)

hours = df0 - df1
df['HOURS'] = hours
df = df.fillna(1)
print df

# print df[['Age']][(df['Sex']=="male") & (df['Survived']==1)].apply(numpy.mean)
