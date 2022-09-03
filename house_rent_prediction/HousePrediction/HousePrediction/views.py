from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import  metrics


def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv(r"C:\Users\rsp.tech Solution\OneDrive\Desktop\Django Prediction Projects\house_rent_prediction\HousePrediction\USA_Housing.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= .30)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
   

    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))

    pred = round(pred[0])

    price = "The Predicted Rent Is Rs "+str(pred)
    return render(request, 'predict.html', {"result2":price}) 