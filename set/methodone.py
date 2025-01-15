#  clear()
set1={"elmehdi","tabi",18}
set1.clear()
print(set1)

# union 
a={"one","two","three"}
b={1,2,3}
c={"elmehdi","cool"}

print(a|b|c)
print(a.union(b,c))

# add 
setone={1,2,3,4}
# setone.add(5,6)set.add() takes exactly one argument (2 given)
setone.add(5)
setone.add(6)
print(setone)

# copy  => set is shallow copy
 
g={"tb","18 ans" , True}
f=g.copy()
print(g)
print(f)
g={"tb","18 ans" , True , "hhh"}
print(g)
print(f)

# remove => si il y a une élment qui t'es acrie il est suprime , sinon il affiche erro 
w={1,2,3,4}
w.remove(1)
print(w)
# w.remove(5)
# print(w) => error 

#& discard()=>  si il y a  rien une  élment qui t'es acrie il est suprime il fait rien  

x={1,2,3,4}
x.discard(1)
print(x)
w.discard(5)
print(w) 

#* pop()
i={"a" , False ,'elmehdi',12,5}
print(i.pop())

#! update  => comme union mais il est unique 

j={1,2,3}
k={1,"a","b","c",2}
b=["one",1,"hehe"]
j.update(k,b)
print(j)