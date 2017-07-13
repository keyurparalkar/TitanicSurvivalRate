import pandas
import numpy


df = pandas.read_csv("train.csv")

print df[['PassengerId','Survived','Age','Sex','Pclass']][(df["Sex"]=="female") & (df["Survived"]==1)] #females
print ""

print df[['PassengerId','Survived','Age','Sex','Pclass']][( (df["Sex"]=="male") | (df["Sex"]=="female") ) & (df['Pclass']==1) & (df['Age']<18) & (df['Survived']==1) ]
