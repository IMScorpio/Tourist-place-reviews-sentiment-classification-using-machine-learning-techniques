from django.shortcuts import render
from pyexpat.errors import messages
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import mysql.connector
import mysql
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB


def index(request):
    return render(request,"index.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminhome(request):
    return render(request,'admin/adminhome.html')

def adminloginaction(request):
    if request.method == "POST":
        #if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return render(request,'admin/adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    return render(request,'adminlogin.html')

def logout(request):
    return render(request,'index.html')

def rf(request):
    dataset = pd.read_csv("google_review_ratings.csv",header=1)
    #print(train.shape)
    dataset =  dataset.fillna(dataset.mean())
    accuracy = 0.9
    X = dataset.iloc[:,6:10].values
    y = dataset.iloc[:,7].values
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.25)
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import accuracy_score

    # create regressor object
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)

    # fit the regressor with x and y data
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    acc=accuracy_score(y_pred.round(),y_test.round())
    print("y value:",y_pred)
    print("acc",acc)

    return render(request,'admin/rf.html',{"accuracy":acc})

def svm(request):
    dataset = pd.read_csv("google_review_ratings.csv", header=1)
    # print(train.shape)
    dataset = dataset.fillna(dataset.mean())
    X = dataset.iloc[:, 6:10].values
    y = dataset.iloc[:, -2].values
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    from sklearn.svm import SVR
    # X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=1/3,random_state=0)
    svclassifier = SVR(kernel='linear')
    svclassifier.fit(X_train,y_train)

    #print(svclassifier.predict([0.58, 0.76]))
    # clf = svm.SVR()
    # clf.fit(X_train, trainingScores)
    # print("SVR")
    # print(clf.predict(predictionData))
    y_pred = svclassifier.predict(X_test)
    # m = confusion_matrix(y_test,y_pred)
    # accurancy = classification_report(y_test, y_pred)
    # accuracy_score(y_true, y_pred, normalize=False)
    accurancy=accuracy_score(y_test.round(), y_pred.round(), normalize=False)
    accurancy1=(accurancy/1000)
    # y_pred =(y_pred > 0.5)
    # accuracy_score(y_true, y_pred, normalize=False)
    # print(m)
    print("Accuracy is ",accurancy1)
    return render(request, 'admin/svm.html', {"acc":accurancy1})

def naviebyes(request):
    data = pd.read_csv('google_review_ratings.csv')
    data = data.fillna(data.mean())
    #data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print("data-label:",data.label)
    dataset = data.iloc[:,[6,7]].values
    print("x",dataset)
    dataset1 = data.iloc[:,-1].values
    print("y",dataset1)
    print("shape",dataset.shape)


    dataset = datasets.load_iris()
    model = GaussianNB()
    model.fit(dataset.data, dataset.target)
    expected = dataset.target
    predicted = model.predict(dataset.data)
    accurancy = metrics.classification_report(expected, predicted)
    print("accurancy",accurancy)
    # print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))
    x = accurancy.split()
    print("Toctal splits ",len(x))
    dict = {

        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],
        'len32': x[32],
        'len33': x[33],


    }
    return render(request, 'admin/navieaccuracy.html', dict)
