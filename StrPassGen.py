import string 
import random

list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.punctuation)
list4 = list(string.digits)

num = input("How Many Characters For The Password ? ")

while True:
    try:
        num = int(num)
        if num < 6 :
            print("Some thing Wronge , You should enter at least 6")
            num = input("Enter the Number : ")

        else:
            break

    except ValueError:
        print("Error, Enter numbers only ")   
        num = input("Enter the Number : ")    


random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

percent1 = round(num * (35/100))
percent2 = round(num * (15/100))

password =[]

for i in range(percent1):
    password.append(list1[i])
    password.append(list2[i])

for i in range(percent2):
    password.append(list3[i])
    password.append(list4[i])    

random.shuffle(password)
password = "".join(password[0:])    


print(password)