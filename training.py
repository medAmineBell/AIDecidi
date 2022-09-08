import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import pickle
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing

df = pd.read_csv('BAC_ECO.csv')
print(df.head())
#info
#columns = ['Bac','Moyenne','BD','TIC','Algo','Math','Physique','Francais','Arabe','Anglais','Philo','Sport','Option']
#sport
#columns = ['Bac','Moyenne','SpecialiteSport','Sport','Science','Physique','Math','Anglais','Francais','Arabe','Philo','Info']
#eco
columns = ['Bac','Moyenne','Economie','Gestion','Math','HistoireGeographie','Anglais','Francais','Arabe','Philo','Info','Sport','Option']
#tech
#columns = ['Bac','Moyenne','ElectriqueMecanique','Math','Physique','Anglais','Francais','Arabe','Philo','Info','TechnologieAppliquee','Sport','Option']
#math
#columns = ['Bac','Moyenne','Physique','Science','Math','Anglais','Francais','Arabe','Philo','Info','Sport','Option']
#lettre
#columns = ['Bac','Moyenne','Philo','Option','Arabe','HistoireGeographie','Anglais','Francais','PhiloIslamique','Info','Sport']
labels = df['Code'].values
features = df[list(columns)].values
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)  # for trainnig and testing
clf = RandomForestClassifier(n_estimators=15)
clf = clf.fit(x_train, y_train)


accuracy = clf.score(x_train, y_train)
print('performance of training data before', accuracy * 100)
acc = clf.score(x_test, y_test)
print('performance of testing data before', acc * 100)
ypredict = clf.predict(x_train)
#print("\n Confusion matrix of traiting \n", confusion_matrix(y_train, ypredict))
ypredict1 = clf.predict(x_test)
#print("\n Confusion matrix of testing \n", confusion_matrix(y_test, ypredict1))
with open('model_bac_eco', 'wb') as f:
    pickle.dump(clf, f)