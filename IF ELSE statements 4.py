#it's been 2 days without opening my laptop 
#kinda mad, but i spent a great weekend though :)

#if statement is one of the necessary tools to code 

#the comparison operator you need : 

#Equal : ==
#Grater than : >
#Less than : <
#Grater or equal to : >=
#Less than or equal to : <=

#---------------------------------------------------

#let's start with a simple one 
if 4>2 : 
    print("true")

#---------------------------------------------------
if 4<2 :
    print('true')

#if the comparing was false it won't show you any result but... we have else statement 
#let's play a simple game

name=input("enter your name:\n")

N=input("hello " + name + " pick a number between 1 and 10: \n ")

if int(N)==6 : 
    print("you won the lottery bi*ch")
else: 
    print("loser")

#you can use more than else statement depends on how many results you have


N=input(name + " we'll give you a secondf chance, pick another number \n ")

if int(N)==6 : 
    print("you won the lottery bi*ch")
else: 
    print("loser")

#now what if we have more than two results. Thats when we need to use the elif statement


A=input("In this list pick a number that may interests you.\n 1: DMT \n 2: shrooms \n 3: LSD, \n")
      
if   A == 1:
        print("""DMT produces effects similar to those of psychedelics, like LSD and magic mushrooms. 
              Some people refer to the drug by other names including Dimitri and fantasia.""")
elif A == 2 :
        print("""Shrooms, also known as magic mushrooms, are wild or cultivated mushrooms that contain psilocybin, 
              a naturally occurring psychoactive and hallucinogenic compound. 
              Some research suggests this substance may help relieve symptoms of some mental health conditions""")
elif A ==3 :
        print("""LSD (lysergic acid diethylamide) is a potent synthetic psychedelic drug1234. 
              It belongs to a class of drugs called hallucinogens and is made from lysergic acid, 
              a fungus that grows on grains like rye3. LSD is not found naturally, but is considered semi-synthetic, 
              as it was first prepared by Albert Hofmann by altering a molecule found in the ergot fungus4.""")
else :
     print("you have to pick a number between 1..3") #the last else statement is optinal depends on your needs
