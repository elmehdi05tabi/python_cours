# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------
 
the_file = None 
the_tries = 5 
while the_tries > 0 :
    try : #! try to oppen file 
         print(f"{the_tries}nombre of thries ".capitalize())
         print("exemple : C:\dossier\file.extention".capitalize())
         file_name_and_path = input("entre le nome de fille => ").strip().capitalize()
         the_file = open(file_name_and_path,"r")
         print(the_file.read())
         break
    except FileNotFoundError: 
        print("the file note fond plus sure the name valid".capitalize())
        the_tries-=1
    except : 
        print("error happen ".capitalize())
    finally : 
        if the_file is not None: 
           the_file.close()
           print("file closed .".capitalize())
else : 
    print("all trice is done".capitalize())
