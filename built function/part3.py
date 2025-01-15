# -----------------------------
# --- built in function---
# -----------------------------
# abs()
# pow()
# min()
# max()
# slice()
# -----------------------------
# abd()
print(abs(100))
print(abs(-100))
print(abs(10.15))
print(abs(-10.15))
print("="*50)
#  pow (base , exp , mod ) => power  
print(pow(2,5)) # => 2*2*2*2*2 => 32 
print(pow(2,5,10)) # => (2*2*2*2*2) % 10 => 2 
print("="*50)

# min(ite,item,item,item)
mytypel = (10 , 50 ,60 , -100 ,30 )
print(min(10 , 2 ,15 -25 ,3 ))  
print(min("elmehdi","k","s","coucou"))
print(min(mytypel))
print("="*50)
# max(ite,item,item,item)
mytypel = (10 , 50 ,60 , -100 ,30 )
print(max(10 , 2 ,15 -25 ,3 ))  
print(max("elmehdi","k","s","coucou"))
print(max(mytypel))
print("="*50)

# slice(start ,end ,step ) => slicing 
a = ["a","b","c","d","e","f"]
print(a[slice(5)])
print(a[slice(2,5,2)])