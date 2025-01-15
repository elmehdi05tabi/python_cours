# -------------------------------------- -------------
# -- function packing , unpacking argumnets *args ----
# -------------------------------------- -------------
# print (1,2,3,4)
# ls = [1,2,3,4]
# print(*ls)
# -------------------------------------- -------------

# def sey_hello(*name) :
#     for i in name :
#      print(f"hello {i}")
# sey_hello ("elemhdi","tabi","rajwi","saad",True)

# -------------------------------------- -------------

def show_details(name,*skill) :
    print(f"hello {name} your skills is :")
    for skills in skill : 
        print(skills) 
print(show_details("elmehdi","html","css","js","mysql","python"))