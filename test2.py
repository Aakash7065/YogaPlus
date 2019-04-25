import pandas as pd

data = pd.read_csv('Bend_t.csv')
data = data.drop(data.columns[0], axis=1)
data.insert(loc=0, column='Pose', value='Plank')
f = open('Bend_t.csv', 'w')
data.to_csv(f, header=True)
f.close()
print(data.shape)
