#  Important Info => Part foor 
myfile = open(r"C:\python\files_heindlign\info.txt" , "a")
# myfile.write("Hello This Is Imprtant Info ! ")
# myfile.truncate(5)  # find the 5 lettre end return it 
# print(myfile.tell()) # give you the posation the cursor  => new line in windows is 2 note 1 
myfile = open(r"C:\python\files_heindlign\info.txt" , "r")
myfile.seek(11) # go in the 6 position 
print(myfile.read())
