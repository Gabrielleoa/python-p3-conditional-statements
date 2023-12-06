#!/usr/bin/env python3

def admin_login(username, password):
    if username == 'admin' or 'ADMIN' and password == '12345':
        return 'Access granted'
    else:
        if username != 'admin' and password != '12345':
         return 'Access denied'
admin_login('sudo', '12345')
def hows_the_weather(temperature):
    if(temperature < 40):
     response = "brisk "
    elif (temperature >= 40 and temperature <= 65):
       response =  'a little chilly'
    elif(temperature > 85):
       response = 'too dang hot'
    else:
       return 'Perfect'
    print(f"It's {response} out there!")
hows_the_weather(99)

def fizzbuzz(num):
    if(num % 3 == 0 and num % 5 == 0):
       print("Fizzbuzz")
    elif (num % 3 == 0):
       print("Fizz")
    elif(num % 5 == 0):
       print("Buzz")
    else:
       print(num)
fizzbuzz(2)
fizzbuzz(25)
fizzbuzz(15)
       
    

def calculator(operation, num1, num2):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
       print(num1 - num2)
    elif operation == "*":
       print(num1 *num2)
    elif operation == "/":
       print(num1/num2)
    else:
       print("Invalid operation!")
calculator("+", 1, 1)
calculator("-", 3, 1)
calculator("*", 3, 2)
calculator("/", 4, 2)
calculator("nope", 4, 2)

