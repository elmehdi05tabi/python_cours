# tuple with one elment 

tuple1=("elmehdi")
tuple2="elmehdi"
print(type(tuple1))
print(type(tuple2))

tuple3=("elmehdi",)
tuple4="elmehdi",
print(type(tuple3))
print(type(tuple4))

tuple3=("elmehdi",)
tuple4="elmehdi",
print(len(tuple3))
print(len(tuple4))

# tuple conacatine 

a=(1,2,3,4)
b=(5,6,7,8)
c=a+ ('is me' , 12 , 5 , True )+b
print(c)

# tuple list sting repeat (*)

mysitng="elmehdi"
mylist=[1,3]
mytuple=("A","B")
print(mytuple*6)
print(mylist*6)
print(mysitng*6)

# count ()

a=(1 , 7 ,8 ,9 ,6 ,2 ,7)
print(a.count(7))

# index()
b=(1 , 7 ,8 ,9 ,6 ,2 ,7)
print(" the position of 9 is:{:d}".format(b.index(9)))
print(f" the position of 9 is:{b.index(9)}")


#  destruct 
a=("a","n","f")
x,y,z =a
print(x)
print(y)
print(z)

a=("a",4,"n","f")
x,_,y,z =a
print(x)
print(y)
print(z)