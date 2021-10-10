#redundant code below for reference

#import  random
#import  string
#lower = string.ascii_lowercase
#upper = string.ascii_uppercase
#digit = string.digits
#charcter = string.punctuation

#if __name__ == '__main__':
#
#    while True:
#        user = int(input("enter the length of password: "))
#        password = []
#        password.extend(list(upper))
#       password.extend(list(lower))
#        password.extend(list(digit))
#        password.extend(list(charcter))
#        random.shuffle(password)
#        print("".join(password[0:user]))

#Newer random password generator using secrets library

import secrets

pass_len = int(input("Enter length of password: "))

print(secrets.token_urlsafe(pass_len))
