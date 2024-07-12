#if you're dumb in math it's okay this will make it easy for you, and don't feel bad i fucked it up too in many ways.
#especially the za was too good but i ended up now in mid july with many stuff to do 
#so it's okay it's never too late but it's time to do something
#====================================================================================================================

# / : devide
# + : add
# - : sub
# * : multiply
# ** : power

X=6

name=input("what's your name \n")
print(name)


print(type(name))#This will show you the variable type that you have ( str is for string )
print("\n")
print(type(X))#X is a integer 

C=X/4

print(C)
print(type(C))#C is a float type

print(X**5)#X power 5

N=input("please pick a multiplyer for X \n")#okay here is a new thing when using the input function it will return a string even if you type an int 

# so we can't multiply int * str so what to do ? 
#we will use the converting data function type(data)
#don't be a dumb and convert alphabets into integer IT WON4T WORK!!
print(type(N))
N=int(N)#N will become an int for good
print(type(N))

X=X*N
print(X) 
#or you don't wanna convert it for good and still want to leave it in str type
X=X*int(N)
print(X)#the result of X will not be the same as the previous one because we have returned X as X*N 




