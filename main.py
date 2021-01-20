d1={"talib": {"Course": "btech", "branch": "cs"}, "saif": "civil"}
print(d1["talib"]["branch"])

age = int(input())
if age<17 or age>60:
    print("you cannot drive")
elif age==18:
    print("we'll think")
elif age>18:
    print("you can drive")
else:
    print("no you cant")