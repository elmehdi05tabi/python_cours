#differnet => le diference entre deux set  
a= {1,2,3,4}
b={"one","two",1,2}
print(a)
print(a.difference(b)) # a-b
print("="*40) #separateure 
#difference_update()
c= {1,2,3,4}
d={"one","two",1,2}
print(c)
c.difference_update(d)
print(c) # a-b
print("="*40)
# intersection() => 
e={1,2,3,4,"x","elmehdi"}
f={"elmehdi",2,"jeje"}
print(e)
print(e.intersection(f)) # e & f
print(e)
print("="*40)
# intersection_update() => 
j={1,2,3,4,"x","elmehdi"}
k={"elmehdi",2,"jeje"}
print(j)
j.intersection_update(k)
print(j)

print("="*40)

# symmetric-difference()
i={1,2,3,4,5,"elmehdi" ,"x"}
l={1,2,4,"elmehdi","x"}
print(i)
print(i.symmetric_difference(l)) # i ^ l
print("="*40)
# symmetric-difference_update()
c={1,2,3,4,5,"elmehdi" ,"x"}
v={1,2,4,"elmehdi","x"}
print(c) 
c.symmetric_difference_update(v)
print(c) 