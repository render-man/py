import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [22, 25, 30],
    'Language': ['English', 'French', 'Spanish']
}

df = pd.DataFrame(data)

gender = ['Female', 'Male', 'Male']

df['Gender'] = gender
#df = df.drop(columns=['Gender'])
df = df.rename(columns={'Name': 'Bruh'})
print(df.get('Gender') is not None)


print(df)
print()
df.loc[len(df)] = ['Hieu', 222, 'C', 'Male']

df.drop(index=[0], axis=0, inplace=True)

print(df)

print('------------------')

#print(df[['Bruh', 'Age']])
print(df.loc[[1, 2, 3], ['Bruh', 'Gender']])
print(df.loc[1, 'Gender'])
print(df.loc[1:2])
print("test")
print(df['Age'] > 30)
print(df.loc[df['Age'] > 30])
#iloc
print("iloc-----")
print(df)
print(df.iloc[[i for i in range(0, 2)], [0, 3]])
print((df['Age'] > 30).tolist())
print(df.iloc[(df['Age'] > 30).tolist()])

