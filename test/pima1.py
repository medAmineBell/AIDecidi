import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from firebase import firebase
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import  confusion_matrix
from sklearn import preprocessing
firebase=firebase.FirebaseApplication("https://adolescent-80847.firebaseio.com//",None)
df=pd.read_csv('diabetes.csv')
print(df.head())
columns=['Pregnancies','Glucose','BloodPressure','DiabetesPedigreeFunction','Age']
labels=df['Outcome'].values
features=df[list(columns)].values
x_train,x_test,y_train,y_test=train_test_split(features,labels,test_size=0.3) #for trainnig and testing
clf=RandomForestClassifier(n_estimators=15)
clf=clf.fit(x_train,y_train)
accuracy=clf.score(x_train,y_train)
print('performance of training data before',accuracy*100)
acc=clf.score(x_test,y_test)
print('performance of testing data before',acc*100)
ypredict=clf.predict(x_train)
print ("\n Confusion matrix of traiting \n", confusion_matrix(y_train, ypredict))
ypredict1=clf.predict(x_test)
print ("\n Confusion matrix of testing \n", confusion_matrix(y_test, ypredict1))

result1 = firebase.get('/ado', '')
print(result1)
nbdia=len(result1)
print("loula bel kol nbdia = "+str(nbdia))
for p_id, p_info in result1.items():
    print("\nPerson ID:", p_id)
    #for key in p_info:
    #print(key + ':', p_info[key])
    if p_info['outcome'] == "":
      print("need to test")
      s=clf.predict([[p_info['pregnancies'], p_info['glucose'], p_info['bloodPressure'], p_info['diabetesPedigreeFunction'], p_info['age']]])
      print(s)
      print(type(s))
      ts = s.tostring()
      print(type(ts))
      ss=int.from_bytes(ts, "little")
      print(ss)
      print(type(ss))
      f=str(ss)
      firebase.put('/ado/'+p_info['id'], 'outcome', f)
while nbdia > 0:
  print("nbdia = "+str(nbdia))
  time.sleep(10)
  print("t3adet 10 sec")
  result2 = firebase.get('/ado', '')
  nbdia1 = len(result2)
  print("nbdia1 = " + str(nbdia1))
  if nbdia1>nbdia :
    for p_id, p_info in result2.items():
      print("\nPerson ID:", p_id)
      # for key in p_info:
      # print(key + ':', p_info[key])
      if p_info['outcome'] == "":
        print("need to test")
        s = clf.predict([[p_info['pregnancies'], p_info['glucose'], p_info['bloodPressure'],
                          p_info['diabetesPedigreeFunction'], p_info['age']]])
        print(s)
        print(type(s))
        ts = s.tostring()
        print(type(ts))
        ss = int.from_bytes(ts, "little")
        print(ss)
        print(type(ss))
        f = str(ss)
        firebase.put('/ado/' + p_info['id'], 'outcome', f)
    nbdia=nbdia1