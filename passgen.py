import random
def GetStrongPassword(length):
    password = ""
    for num in range(1, length + 1):
        password += letters[random.randint(0,len(letters))]

    return password

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=/.-")
length = int(input("What is the length of password? "))

print(GetStrongPassword(length))


