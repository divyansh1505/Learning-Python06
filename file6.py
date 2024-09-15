# with open("ass.txt", "r") as f:    #isko use krke kroge to operation on closed while ka error aayega
#     contents  = f.read()

f = open("ass.txt", "r")
contents = f.read()
f.close()    #read krke uska data ek variable me store krke bnd krdi file 
contents_new = contents.replace("Donkey", "######").replace("donkey", "######")
# contents_new = contents.replace("Donkey" or "donkey", "######") - Dont write ese

if ("Donkey"  in contents or "donkey" in contents):
    print("This file might contain sensitive content")
    ans = input("Do you wish to censor it? : ")
    if (ans == "Yes" or ans == "yes"):
        f = open("ass.txt", "w")
        f.write(contents_new)
        print("File has been updated")
        f.close()
    elif(ans == "No" or ans == "no"):
        print("Okay, No changes made")
        
else:
    print("Have a good day")



       