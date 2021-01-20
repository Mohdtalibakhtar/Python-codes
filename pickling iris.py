import requests
import pickle
#
# r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(r)
#
# l1=r.split("\n")
# print(l1)
#
# l2=[item.split(",") for item in l1]
# print(l2)
#
# with open("irispickle.pkl", 'wb') as f:
#     pickle.dump(l2,f)

with open("irispickle.pkl", 'rb') as f:
    print(pickle.load(f))