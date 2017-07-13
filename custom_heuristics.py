import pandas
import numpy,collections


df = pandas.read_csv("train.csv")

print df[['Survived','Age','Pclass','Fare']][(df['Age']<18) & (df['SibSp']<2) & (df['Parch']>0)]
print ""


print df[['Survived','Age','Pclass','Fare']][(df['Survived']==1) & (df['Fare']>300) & (df['Fare']<400) ]
#print collections.Counter(df['Pclass'][(df['Survived']==1) &(df['Sex']=="male")])
# print ""
#
# print collections.Counter(df['Parch'][(df['Survived']==1) &(df['Sex']=="male")])
# print ""
#
# print "Age :",collections.Counter(df['Age'][(df['Survived']==1) &(df['Sex']=="male")])
