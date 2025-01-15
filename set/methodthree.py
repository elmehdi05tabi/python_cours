# issuperset() => 
a={1,2,3,4}
b={1,2,3,}
c={1,2,3,4,5}
print(a.issuperset(b))  #True 
print(a.issuperset(c)) # False

print("="*40)

# issubset 
a={1,2,3,4}
b={1,2,3,}
c={1,2,3,4,5}
print(a.issubset(b))  #False 
print(a.issubset(c)) # True
print("="*40)

# isdisjoint 
a={1,2,3,4}
b={1,2,3,}
c={11 ,12 ,30}
print(a.isdisjoint(b))  #False 
print(a.isdisjoint(c)) # True
print("="*40)
