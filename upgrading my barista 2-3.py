#I will try to use every previous thing we have learnt


price=6

name=input("good morning sir what is your name ?\n")

print("hello " + name + ", welcome to our coffe shop! ")

menu=("latte, cppucino, espresso, americano \n")

order=input("do you need anything from our menu ? we have: " + menu +"\n")

quantity=input("sounds good and how many " + order + " would you like to order ? \n")

#now we have to calculate the total price of the order and tyo do so we have to convert the QT into integer
total=price*int(quantity)

print("\n")

#another thing when using print function that contain a string we can't add an integer it's like doing a mathematic equation (str+int)=ERROR! 
#so we have to convert the total into a string you can try without converting and it will show you an error 
print("okay " + name + ", your total order will be " + str(total) + "$ and will be ready in few moments please take a seat! ")

