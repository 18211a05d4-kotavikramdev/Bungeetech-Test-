import pandas as pd
data = pd.read_csv('../../input/question-1/main.csv')
del data["Total"]
population = data["Population"]
popul = []
for i in range(9, len(population) + 1, 10):
    popul.append(population.iloc[i])
popul.append(int(population.iloc[-1]))
del data["Population"]
data = data.groupby((data.Year//10)*10).sum()
data.insert(loc = 1, column = 'Population', value = popul)
del data["Year"]
# print(data)
data.to_csv('main.csv')