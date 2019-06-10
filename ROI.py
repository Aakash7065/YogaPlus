import pandas as pd
import math
import numpy as np


class Angle:
    def dist(self, x1, y1, x2, y2):
        return math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    def angle(self, A_x, A_y, B_x, B_y, C_x, C_y):
        a = self.dist(B_x, B_y, C_x, C_y)
        b = self.dist(A_x, A_y, C_x, C_y)
        c = self.dist(B_x, B_y, A_x, A_y)
        cosa = (b * b + c * c - a * a) / (2 * b * c)
        radian = math.acos(cosa)
        return radian * 180 / 3.14

    def one(self, data):
        temp = data.apply(
            lambda x: self.angle(x.leftShoulder_x, x.leftShoulder_y, x.leftElbow_x, x.leftElbow_y, x.leftHip_x,
                                 x.leftHip_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def two(self, data):
        temp = data.apply(
            lambda x: self.angle(x.leftElbow_x, x.leftElbow_y, x.leftWrist_x, x.leftWrist_y, x.leftShoulder_x,
                                 x.leftShoulder_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def three(self, data):
        temp = data.apply(
            lambda x: self.angle(x.leftHip_x, x.leftHip_y, x.leftKnee_x, x.leftKnee_y, x.leftShoulder_x,
                                 x.leftShoulder_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def four(self, data):
        temp = data.apply(
            lambda x: self.angle(x.leftKnee_x, x.leftKnee_y, x.leftAnkle_x, x.leftAnkle_y, x.leftHip_x,
                                 x.leftHip_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def five(self, data):
        temp = data.apply(
            lambda x: self.angle(x.rightKnee_x, x.rightKnee_y, x.rightAnkle_x, x.rightAnkle_y, x.rightHip_x,
                                 x.rightHip_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def six(self, data):
        temp = data.apply(
            lambda x: self.angle(x.rightHip_x, x.rightHip_y, x.rightKnee_x, x.rightKnee_y, x.rightShoulder_x,
                                 x.rightShoulder_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def seven(self, data):
        temp = data.apply(
            lambda x: self.angle(x.rightShoulder_x, x.rightShoulder_y, x.rightHip_x, x.rightHip_y, x.rightElbow_x,
                                 x.rightElbow_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def eight(self, data):
        temp = data.apply(
            lambda x: self.angle(x.rightElbow_x, x.rightElbow_y, x.rightShoulder_x, x.rightShoulder_y, x.rightWrist_x,
                                 x.rightWrist_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def nine(self, data):
        temp = data.apply(
            lambda x: self.angle(x.leftShoulder_x, x.leftShoulder_y, x.leftElbow_x, x.leftElbow_y, x.rightShoulder_x,
                                 x.rightShoulder_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def ten(self, data):
        temp = data.apply(
            lambda x: self.angle(x.rightShoulder_x, x.rightShoulder_y, x.leftShoulder_x, x.leftShoulder_y,
                                 x.rightElbow_x,
                                 x.rightElbow_y),
            axis=1)
        # print(temp)
        return np.median(temp)

    def all(self, data):
        angles =[]
        angles.append(self.one(data))
        angles.append(self.two(data))
        angles.append(self.three(data))
        angles.append(self.four(data))
        angles.append(self.five(data))
        angles.append(self.six(data))
        angles.append(self.seven(data))
        angles.append(self.eight(data))
        angles.append(self.nine(data))
        angles.append(self.ten(data))
        return angles
        # Pose = data1["Pose"]
        # rest = data1.iloc[:, 1:]
        # one = self.one(rest)
        # two = self.two(rest)
        # three = self.three(rest)
        # four = self.four(rest)
        # five = self.five(rest)
        # six = self.six(rest)
        # seven = self.seven(rest)
        # eight = self.eight(rest)
        # nine = self.nine(rest)
        # ten = self.ten(rest)
        # temp = pd.concat([Pose, one, two, three, four, five, six, seven, eight, nine, ten], axis=1)
        # f = open('Angle.csv', 'a')
        # temp.to_csv(f, header=False)
        # f.close()


class ROI:
    def __init__(self):
        self.temp = Angle()

    def bend(self, data):
        data1 = pd.read_csv('Bend.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def bridge(self, data):
        data1 = pd.read_csv('Bridge.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def child(self, data):
        data1 = pd.read_csv('Child.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def downwarddog(self, data):
        data1 = pd.read_csv('DownwardDog.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def mountain(self, data):
        data1 = pd.read_csv('Mountain.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def plank(self, data):
        data1 = pd.read_csv('Plank.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def tree(self, data):
        data1 = pd.read_csv('Tree.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def trianglepose(self, data):
        data1 = pd.read_csv('TrianglePose.csv')
        ideal = self.temp.all(data1)
        real = self.temp.all(data)
        return [ideal, real]

    def warrior1(self, data):
        data1 = pd.read_csv('Warrior1.csv')
        ideal = Angle.all(data1)
        real = Angle.all(data)
        return [ideal, real]
