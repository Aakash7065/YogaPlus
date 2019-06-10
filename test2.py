import pandas as pd
from ROI import Angle
# data = pd.read_csv('Warrior1.csv')
# data = data.drop(data.columns[0], axis=1)
# data.insert(loc=0, column='Pose', value='Warrior1')
# f = open('Warrior1.csv', 'w')
# data.to_csv(f, header=True)
# f.close()
# print(data.shape)

# test = Angle()
data1 = pd.read_csv('TrianglePose.csv')
print(type(data1))
# angles = test.all(data1)
