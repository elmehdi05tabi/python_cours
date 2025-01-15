#  new formating 
name="elmehdi"
age=19
cp=22
print("my name is :"+name)
# print("may name is :"+name+"and my age is "+age) => error
print("my name is :{} and my age is:{} my code postale is:{}".format(name,age,cp))
print("my name is :{:s} and my age is:{:d} my code postale is:{:f}".format(name,age,cp))

# %{:s} => string
# %{:d} => numbre
# %{:f} => float f
# changer le nombre de zero en %f 

a=20
print("mon score est {:.2f}".format(a))
print("mon score est {:.2f}".format(a))

#truncite string 
a2="je vais bien et vous "
print ("bonjour mon ami comment tu-vas{:.12s}".format(a2))

# mon argent 
arg=551203501687
print("j'ai dans une mon compte banquire {:d} ".format(arg))
print("j'ai dans une mon compte banquire {:_d} ".format(arg))
print("j'ai dans une mon compte banquire {:,d} ".format(arg))
# print("j'ai dans une mon compte banquire {:&d} ".format(arg)) => error      


# rearrangr   item 
a , b ,c =12 ,15 ,22
print ("{2},{0},{1}".format(a,b,c)) # 22 12 15
print ("{1},{2},{0}".format(a,b,c)) # 15 22 12
print ("{0},{2},{1}".format(a,b,c)) # 12 22 15 

# format in version 3.6 

x="elmehdi"
z ="tabi"
w =18
print (f"je m'appelle {x} et mon nom est {z} et j'ai {w}") 