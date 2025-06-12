import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 26, 30],
    'Language': ['English', 'French', 'Spanish']
}

df = pd.DataFrame(data)

print(df)
print('-------------')
i = df['Name'].tolist()
print(df.iloc[i.index('Alice')])
print(df.iloc[2])
print("NNLT")
print(df.loc[(df['Age'] > 20) & (df['Age'] <= 30), 'Language'])
print("2 head")
print(df.head(2))

print('change---')
df.loc[df['Name'] == 'Bob', 'Language'] = 'Hehe'
print(df)
