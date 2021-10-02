import pandas as pd
data = pd.read_csv('../../input/question-3/main.csv')
data = data[["Team", "Yellow Cards", "Red Cards"]]
result = data.sort_values(by = ['Red Cards', 'Yellow Cards'], ascending = False)
# print(result)
result.to_csv('main.csv')