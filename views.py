from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score



# our home page view
def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(ph, hardness, solids,chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity, potability):
    import pickle
    model = pickle.load(open("waterpotability.sav", "rb"))
    scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict(sc.transform([[ph, hardness, solids,chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity, potability]]))

    if potability == 0:
        return "not safe"
    elif potability == 1:
        return "safe"
    else:
        return "error"


# our result page view
def result(request):
    ph = int(request.GET['ph'])
    hardness = int(request.GET['hardness'])
    solids = int(request.GET['solids'])
    chloramines = int(request.GET['chloramines'])
    sulfate = int(request.GET['sulfate'])
    conductivity = int(request.GET['conductivity'])
    organic_carbon = int(request.GET['organic_carbon'])
    trihalomethanes = int(request.GET['trihalomethanes'])
    turbidity = int(request.GET['turbidity'])

    result = getPredictions(ph, hardness, solids,chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)

    return render(request, 'result.html', {'result': result})
