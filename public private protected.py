class talib():
    var = 10
    _protec= "Protected"
    __privat="Private"
    pass
class saif(talib):
    pass


uzaif= saif()
print(uzaif._protec)
print(uzaif._talib__privat)

tal=talib()
print(tal._talib__privat)