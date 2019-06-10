import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix

data1 = pd.read_csv('Mountain.csv')
data2 = pd.read_csv('Bend.csv')
data4 = pd.read_csv('Bridge.csv')
data5 = pd.read_csv('Child.csv')
data6 = pd.read_csv('DownwardDog.csv')
data7 = pd.read_csv('Plank.csv')
data8 = pd.read_csv('Tree.csv')
data9 = pd.read_csv('TrianglePose.csv')
data10 = pd.read_csv('Warrior1.csv')
data11 = [data1, data2, data4, data5, data6, data7, data8, data9, data10]
data = pd.concat(data11)
# print(data.shape)
# y_train = data.Pose
# X_train = data.drop('Pose', axis=1)
# data_1 = pd.read_csv('Child_t.csv')
# y_test = data_1.Pose
# X_test = data_1.drop('Pose', axis=1)
y= data.Pose
X = data.drop('Pose',axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
# classifier = KNeighborsClassifier(n_neighbors=4)
classifier = svm.SVC()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(y_pred)
