
import  random
import  string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
charcter = string.punctuation

if __name__ == '__main__':

    while True:
        user = int(input("enter the length of password: "))
        password = []
        password.extend(list(upper))
        password.extend(list(lower))
        password.extend(list(digit))
        password.extend(list(charcter))
        random.shuffle(password)
        print("".join(password[0:user]))
