#so let's upgrade our barista using if statement 

price=0
order=0
name=input("good morning sir what is your name ?\n")

if name== "Firas": #don't forget to put "" if your gonna compare with a string 
   print("Ahh hello mr " + name + ", welcome again to our coffe shop! ")
else :
    print("hello " + name + ", welcome to our coffe shop! ")


menu=("latte, cppucino, espresso, americano \n")

order=input("do you need anything from our menu ? we have: " + menu +"\n")

quantity=input("sounds good and how many " + order + " would you like to order ? \n")

if order=="latte" :
   price=6.5#the price is a float type
elif order=="cappucino" :
   price=7
elif order=="espresso" :
   price=7
elif order=="americano" :
   price=4
else :
   print("we're sorry but i think we don't have such an order in our menu !")  
   
total=price*int(quantity)

print("\n")

print("okay " + name + ", your total order will be " + str(total) + "$ and will be ready in few moments please take a seat! ")

#the last meesage is ueless when you select an order that doesn't exist but it's fixible by using other statement 
#but for now i can't do shit while i'm listening to BLACK COFFEE style | afro house by DJ ALBO mix 2024 