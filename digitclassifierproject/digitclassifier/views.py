from django.shortcuts import render
import csv
import pandas as pd
from sklearn import tree
from django.http import JsonResponse


# Create your views here.
def home(request):
    global prediction
    image_data = request.GET.get('image_data')
    if image_data:
        image_data = image_data.split(',')
        image_data[0] = image_data[0][1]
        image_data[-1] = image_data[-1][0]
        image_array = list(map(int,image_data))
        digit = request.GET.get('Digit')
        print(digit)
        image_array.append(digit)
        # image_array = np.reshape(image_data,(8,8))
        # with open('Dataset.csv', mode = 'a', newline='') as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     # Write the new data to the CSV file
        #     csv_writer.writerow(image_array)
    return render(request, 'home.html',{'result' : f" Draw n Check "})


def result(request):
    image_data = request.GET.get('image_data')
    if image_data:
        image_data = image_data.split(',')
        image_data[0] = image_data[0][1]
        image_data[-1] = image_data[-1][0]
        image_array = list(map(int,image_data))
    Data = pd.read_csv("Dataset.csv")
    y = Data['digit']
    Data = Data.drop(['digit'], axis = 1)
    X = Data.to_numpy()
    model = tree.DecisionTreeClassifier()
    model.fit(X, y)
    prediction = model.predict([image_array])[0]
    print(prediction)
    response_data = {'result': f" Prediction: {prediction}"}
    return JsonResponse(response_data)

def predict(request):
    global prediction
    return render(request, 'home.html', {'result' : f"Prediction : {prediction}"})