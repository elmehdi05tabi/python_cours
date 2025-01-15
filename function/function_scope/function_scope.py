# ----------------------
# --- function scope --- 
# ----------------------
x = 10 # this is globel value 
def one() :
    global x  
    x=2 
    print(f"print the variable form function scope {x}")
def two() : 
    print(f"print tha varibles after one fuction is callaed {x}")
one()
print (f"print variable from function scope {x}")
two()