import pandas as pd

# Series

data = {
    "Alice" : 85,
    "Bob": 72,
    "Charlie": 90,
    "Daniel" : 85,
    "David": 68
}

se = pd.Series(data, [x for x in data.keys()][0:5])


se["Frank"] = 88

print(se)
print(se.axes[0].tolist())
print(se.values.tolist())
print(se.mean())
print(se[se.idxmax()])
