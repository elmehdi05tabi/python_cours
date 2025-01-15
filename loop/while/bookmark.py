# ===============================
# ========== while loop =========
# ===bookmarks web site  ===
# ========= ==== 

#  empty  list   
myfavoritsit = []
# maximum elment in the list  
maximun = 5 
while maximun > 0 :
    #  input the new web site  
    web= input("select the web sit withot https://")
    #  add the web site in the lest 
    myfavoritsit.append(f"https://{web}".strip().lower())
    maximun -= 1 
    #  print the add message 
    print(f"the web site is add , you have {maximun} place empty")
    # print the list 
    print(myfavoritsit)
else : 
    # finish to add  the web site 
    print("the place is finising ")

index = 0 
#  for print the lite to my favorit web site 
if len(myfavoritsit) > index  :
    #  sort the list 
    myfavoritsit.sort()
    print("the list of the bookmark of the web site :")

    while  index  < len(myfavoritsit) : 
        print(myfavoritsit[index])
        index+=1 
    