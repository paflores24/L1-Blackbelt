import random
a = random.randint(1,10)

while True:
    number = int(input("Guess the number: "));
    if number == a:
        print("Correct!");   
        break
    elif number!= a:
        print("Wrong, try again!"); 
    
