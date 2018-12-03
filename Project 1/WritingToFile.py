#Never read and write to the same file. 
#You only write to the file when you are done everything you want to do. 

print("Start Writing Program")
#Pass your user name in and then you have some file convention
#are files always first inital Last name
#If you use the w parameter that means write over anything that is in teh file. 
#f = open("JKatz.txt","w")
f = open("JKatz.txt","a")

f.write("one\n")
f.write("two\n")

print("End Writing Program")

f.close()

