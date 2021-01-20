secure= (('i' ,'1'), ('s', '$'),('a','@'))

def securepass(password):
    for a,b in secure:
        password=password.replace(a,b)
    return password

if __name__ == '__main__':
    password = input("Enter your password: ")
    password=securepass(password)
    print(f"Your new secure password {password}")