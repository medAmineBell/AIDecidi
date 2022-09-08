import pickle
with open('model_bac_info', 'rb') as f:
    rf = pickle.load(f)              
res = rf.predict([[1,13.4,15.5,17.5,16.5,7.75,7.5,9,11.5,14,9,18.5,19.83]])
print(res)   