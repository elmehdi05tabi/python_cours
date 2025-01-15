#---------------------
#  clear() =>  il est videé la  list 
#---------------------

a = [ 1 ,2 ,3 ,4]
a.clear()
print(a)

#---------------------
# copy ()=> 
#---------------------
b=[ 1,2,3,4]
c=b.copy()
print(b)  #=> main list
print(c) # => copy list 
b.append(5) 
print(b)  #=> main list
print(c) # => copy list 
 
#---------------------
# count() => calculer l'élment commme bien il a dans la list 
#---------------------

# print(d.count(1))

#---------------------
# index() => donne le position de ce index  
#---------------------
n=["elmehdi" ,"tabi" ,"morocco" ,"messi" ,"cr7"]
print(n.index("cr7"))

#---------------------
# insert([position avant ] , [ index])
#---------------------

b = [1,2,3,4,56,7,"test" ,89 ]
b.insert(0,'is me')
print(b)
b.insert(-2,"heheheheh")
print(b)

#---------------------
# pop () => Remove and return item at index (default last).
#---------------------
z=["a",1,"f",7 ,"ee","se",45]
print(z.pop(5))