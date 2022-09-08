

from firebase import firebase
import time
import  pickle

with open('model', 'rb') as f:
    rf = pickle.load(f)

firebase = firebase.FirebaseApplication("https://adolescent-80847.firebaseio.com//", None)
result1 = firebase.get('/gameplay', '')
for p_id, p_info in result1.items():
    if p_info['Outcome'] == "":
        print("need to test")
        s = rf.predict([[p_info['theme'], p_info['music'], p_info['resistance'], p_info['time'],
                                  p_info['nbTentative'], p_info['feedback'], p_info['Anxiety'], p_info['sensOfHearing'],
                                  p_info['continuity']]])
        print(s)
        print(type(s))
        ts = s.tostring()
        print(type(ts))
        ss = int.from_bytes(ts, "little")
        print(ss)
        print(type(ss))
        f = str(ss)
        firebase.put('/gameplay/' + p_id, 'Outcome', f)


