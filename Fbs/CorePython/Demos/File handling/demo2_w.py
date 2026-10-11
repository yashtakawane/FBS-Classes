#write mode-----------------------
# f=open("xyz.txt","w") #"w"(write) module erases existing data and adds given data
# f.write("MI Won % tropies\nCSK is Loser")
# f.writelines(["\ni am in python\ni am good at coding"])#writelines take input as list this is the difference between write and writelines


#append mode

#f=open("xyz.txt","a") #this can be written as below
with open("xyz.txt","a") as f:#this is the alternative to write
    f.write("\nKKR won 2 tropies")
