from ROI import Angle
import pandas as pd

data1 = pd.read_csv('Mountain.csv')
data2 = pd.read_csv('Bend.csv')
data4 = pd.read_csv('Bridge.csv')
data5 = pd.read_csv('Child.csv')
data6 = pd.read_csv('DownwardDog.csv')
data7 = pd.read_csv('Plank.csv')
data9 = pd.read_csv('TrianglePose.csv')
data10 = pd.read_csv('Warrior1.csv')
data11 = [data1, data2, data4, data5, data6, data7, data9, data10]
data = pd.concat(data11)
temp =Angle()
temp.all(data1=data)
