import pickle

# list = ["BMW", "Maruti", "Harley", "Rolce"]
# a = "car.pkl"
# obja= open(a, 'wb')
# pickle.dump(list, obja)
# obja.close()

file = "car.pkl"
fileobj = open(file ,'rb')
a =  pickle.load(fileobj)
print(a)