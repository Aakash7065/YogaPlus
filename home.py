#!/usr/bin/python
import threading

from flask import Flask, render_template, request, redirect, jsonify, json, url_for, g
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from ROI import ROI
from sklearn.metrics import classification_report, confusion_matrix
import json

app = Flask(__name__)

data_g = None


@app.route('/')
def hello_world():
    return render_template("home.html", ideal=None, real=None)


@app.route('/poseROI/<pose1>/')
def poseROI(pose1):
    data = data_g
    print(pose1)
    temp = ROI()
    if pose1 == 'SeatedForwardBend':
        angles = temp.bend(data)
    elif pose1 == 'Bridge':
        angles = temp.bridge(data)
    elif pose1 == 'Child':
        angles = temp.child(data)
    elif pose1 == 'DownwardDog':
        angles = temp.downwarddog(data)
    elif pose1 == 'Mountain':
        angles = temp.mountain(data)
    elif pose1 == 'Plank':
        angles = temp.plank(data)
    elif pose1 == 'Tree':
        angles = temp.tree(data)
    elif pose1 == 'TrianglePose':
        angles = temp.trianglepose(data)
    else:
        angles = temp.warrior1(data)

    ideal = angles[0]
    real = angles[1]
    print(ideal)
    print(real)
    return render_template('pose.html', pose=pose1, ideal=ideal, real=real, len=len(ideal))


@app.route('/human_pose/', methods=['POST', 'GET'])
def human_pose():
    global data_g
    result = request.get_json(force=True)
    # dt(result)
    data1 = json_to_df(result)
    data_g = data1
    pose2 = predict(data1)
    print(pose2)
    return redirect(url_for('poseROI', pose1=pose2[0]))


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


# def js_r(data1):
#     with open(data1, encoding='utf-8') as f_in:
#         return json.load(f_in)


def json_to_df(data):
    my_dic_data = data
    keys = my_dic_data.keys()
    dict_you_want = {'my_items': my_dic_data['keypoints'] for key in keys}
    df = pd.DataFrame(dict_you_want)
    df2 = df['my_items'].apply(pd.Series)
    df2.drop(['score'], axis=1)
    # df2=df2.pivot(columns='part')
    pt = df2['position'].tolist()
    dff = pd.DataFrame(columns=df2['part'])
    dff.loc[len(dff)] = pt
    print(dff)
    for key, value in dff.iteritems():
        dff = pd.concat([dff.drop([key], axis=1), dff[key].apply(pd.Series)], axis=1)
        dff = dff.rename(columns={'x': key + '_x', 'y': key + '_y'})
    return dff


# def format2(data):
#     data = data.drop(data.columns[0], axis=1)
#     print(data.shape)
#     return data


def predict(data_1):
    print(data_1.shape)
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
    print(data.shape)

    y_train = data.Pose
    X_train = data.drop('Pose', axis=1)
    X_test = data_1
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    # classifier1 = KNeighborsClassifier(n_neighbors=3)
    # classifier1.fit(X_train, y_train)

    classifier2 = svm.SVC()
    classifier2.fit(X_train, y_train)

    # y_pred1 = classifier1.predict(X_test)
    y_pred2 = classifier2.predict(X_test)
    return y_pred2


def dt(data):
    if (data['score'] < 0.2):
        print("Not Included")
        return
    dff = json_to_df(data)
    f = open('Warrior1.csv', 'a')
    dff.to_csv(f, header=False)
    f.close()


if __name__ == '__main__':
    app.run(debug=True)
