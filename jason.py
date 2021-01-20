import json

data= '{"1": "Python", "2":"Java"}'
print(data)

parsed = json.loads(data)
print(parsed['1'])

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
print(parsed)


data2= {
    "language": "Python",
    "school": "Jamia"
}

jscomp= json.dumps(data2) #This used to make code compatible to json file
print(jscomp)