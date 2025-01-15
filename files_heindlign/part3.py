# fille inheading => write and append 

# file = open(r"C:\python\files_heindlign\tabi.txt","w")
# file.write("hello elmehdi tabi\n")
# file.write("how ara you : \n")
file = open(r"C:\python\files_heindlign\tabi.txt","a")
l = ["nice","day","is good "]
file.writelines(l)