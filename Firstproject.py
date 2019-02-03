from random import randint

def digit1(z):
    while True:
        x = input(z)
        try:
            x = int(x)
            return x
            break
        except:
            print ("Un prix est un nombre {} n'est pas un nombre".format(x))
            x = input("Un prix : ")


random_number = digit1("Entrer les dernier prix possible : ")

just_price = randint(1, random_number)

condition = 0
trys = 0
while condition == 0:
 
    user_price = digit1("Entrer un prix : ")
    trys = trys + 1
    if user_price == just_price:
        condition =+ 1
        
 
    elif user_price > just_price:
        print("C'est moins")
       
    elif user_price < just_price:
        print("C'est plus")

print("C'est fini." + " Le prix est {}.".format(just_price) + "Tu as fais {} essaies".format(trys))