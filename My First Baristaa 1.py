#after learning the first steps of python, the print, input functions and the variables we now can use them to build a simple coffe shop


name=input("good morning sir what is your name ?\n")

print("hello " + name + ", welcome to our coffe shop! ")

menu=("latte, cppucino, espresso, americano \n")

order=input(name + " do you need anything from our menu ? we have: " + menu)
print("\n")

print("okay " + name + ", your " + order + " will be ready in few moments please take a seat! ")

