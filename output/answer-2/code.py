import pandas as pd
data = pd.read_csv('../../input/question-2/main.csv')
data = data[["age", "occupation"]]
result = data.groupby('occupation').agg({'age': ['min', 'max']})
# print(result)
result.to_csv('main.csv')