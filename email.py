str= "Talib@gmail.com bjbvjebjvncnknscj saif@gmail.com ncjanjvncin google@gmail.com"
print(str)
import re

find = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][0-9a-zA-Z]+", str)
# find= re.findall(r"/w+@/S+/w", str)
# get= find.finditer(str)
# for i in get:
#     print(i)
print(find)