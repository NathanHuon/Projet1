from random import randint

def digit1(z):
    while True:
        x = input(z)
        try:
            x = int(x)
            return x
        except:
            print ("Un prix est un nombre {} n'est pas un nombre".format(x))
            x = input("Un prix : ")


random_number = digit1("Entrer les dernier prix possible : ")

just_price = randint(1, random_number)

print("""
   _           _            
  (_)_   _ ___| |_ ___      
  | | | | / __| __/ _ \     
  | | |_| \__ \ ||  __/     
 _/ |\__,_|___/\__\___|     
|__/                        
            ___      _      
           / _ \_ __(_)_  __
          / /_)/ '__| \ \/ /
         / ___/| |  | |>  < 
         \/    |_|  |_/_/\_\
         
""")



trys = 0

while(True):
 
    user_price = digit1("Entrer un prix : ")
    trys = trys + 1
    if user_price == just_price:
        break
 
    else:
        if user_price > just_price:
            print("C'est moins")
        else:
            if user_price < just_price:
                print("C'est plus")

print("C'est fini." + " Le prix est {}.".format(just_price) + "Tu as fais {} essaies".format(trys))