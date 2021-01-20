import re
address = "Mehrauli - Badarpur Rd, near Batra Hospital Block D, Hamdard Nagar, New Delhi, Delhi "

find = re.compile(r"rd")

get= find.finditer(address)
for i in get:
    print(i)

