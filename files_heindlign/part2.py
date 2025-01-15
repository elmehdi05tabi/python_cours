#  --------------------------
#  -- Part Two :  Read file -- 
#  --------------------------

myfile = open(r"C:\Users\tabi\Desktop\python\files_heindlign\elmehdi.txt","r")
# print(myfile.name)
# print(myfile.mode)
# print(myfile.encoding)
# print(myfile.read())  => for read all the file 
# print(myfile.read(size | -1 )) => default is - 1 for read all the content in the fille 

#  readline ()  => read line by line 

# print(myfile.readline())
# print(myfile.readline(5))
# print(myfile.read(10))

#  for read line a want : 
for line in myfile : 
    print(line)
    if line.startswith("03") :
        break 
myfile.close()
