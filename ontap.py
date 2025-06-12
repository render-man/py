import pandas as pd

data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 39],
    'Department': ['HR', 'IT', 'IT', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)

print(df)

print('Frank'in df['Name'].values)

df.loc[len(df)] = [6, 'Frank', 28, 'Marketing', 65000]

print('----------')
print(df)

#change
df.loc[df['EmployeeID'] == 3, ['Department', 'Salary']] = ['HR', 75000]
print(df)

#del
v = df['EmployeeID'].tolist()
df.drop(index=[v.index(4)], axis=0, inplace=True)
print(df)

#filter
print('------filter----')
print(df.loc[df['Department'] == 'HR'])
print(df.loc[df['Salary'] > 60000])
print(df.loc[(df['Age'] > 20 ) &(df['Department'] == 'IT')])
print(df)
print(df.loc[df['Department'] == 'HR']['Age'].mean())

