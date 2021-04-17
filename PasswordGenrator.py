import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
if __name__ == '__main__':
    userp=int(input("Enter the lenght of the passowrd:"))
    password=[]
    password.extend((list(s1)))
    password.extend((list(s2)))
    password.extend((list(s3)))
    random.shuffle(password)
    print("Your",userp,"digit password is:")
    print("".join(password[0:userp])) #imp we print here


