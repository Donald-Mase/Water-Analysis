import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score



dataset = pd.read_csv("water_potability.csv", encoding='latin-1')
dataset = dataset.rename(columns=lambda x: x.strip().lower())

#cleaning missing values
dataset = dataset.dropna()
dataset.isnull().sum()
dataset = dataset[['ph','hardness','solids','chloramines','sulfate','conductivity','organic_carbon','trihalomethanes','turbidity','potability']]

X = dataset.drop(['potability'], axis=1)
y = dataset['potability']

# scaling features
sc = MinMaxScaler(feature_range=(0,1))
X_scaled = sc.fit_transform(X)

# model fit
log_model = LogisticRegression(C=1)
log_model.fit(X_scaled, y)

# saving model as a pickle
import pickle
pickle.dump(log_model,open("waterpotability.sav", "wb"))
pickle.dump(sc, open("scaler.sav", "wb"))



