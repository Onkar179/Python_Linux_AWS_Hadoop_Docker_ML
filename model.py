import pandas
dataset=pandas.read_csv('salarydata.csv')
y=dataset['Salary']
x=dataset['YearsExperience']
from sklearn.linear_model import LinearRegression
x=x.values
x=x.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
exp=input('\t\t\t\tHow Many Years of Experience you have ? :   ')
print('\t\t\t\tPredicted Salary is :  ')
print(model.predict([[float(exp)]]))
print()
