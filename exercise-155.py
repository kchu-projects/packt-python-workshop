import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix


df = pd.read_csv("data/HTRU_2.csv", header=None)
df.columns = [
    "Mean of integrated profile",
    "Standard deviation of integrated profile",
    "Excess kurtosis of integrated profile",
    "Skewness of integrated profile",
    "Mean of DM-SNR curve",
    "Standard deviation of DM-SNR curve",
    "Excess kurtosis of DM-SNR curve",
    "Skewness of DM-SMR curve",
    "Class"
]

X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

def clf_model(model):
    clf = model
    scores = cross_val_score(clf, X, y)
    print(f"Scores: {scores}")
    print(f"Mean score: {scores.mean()}")


def confusion(model):
    # create a model classifier
    clf = model
    # fit classifier to the data
    clf.fit(X_train, y_train)
    # predict labels of the y_pred test set
    y_pred = clf.predict(X_test)
    print(f"Confusion Matrix: {confusion_matrix(y_test, y_pred)}")
    print(f"Classification Report: {classification_report(y_test, y_pred)}")
    return clf


clf_model(AdaBoostClassifier())
confusion(AdaBoostClassifier())
