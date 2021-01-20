import string
import random

s1=string.ascii_uppercase
# print(s1)
s2=string.ascii_lowercase
# print(s2)
s3=string.digits
# print(s3)
s4=string.punctuation
# print(s4)

letters=[]
letters.extend(s1)
letters.extend(s2)
letters.extend(s3)
letters.extend(s4)
# print(letters)

random.shuffle(letters)
print(letters)

length=int(input("Enter the length of the password : "))
print("".join(letters[0:length]))
