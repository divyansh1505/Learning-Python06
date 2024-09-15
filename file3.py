p = open("poem.txt", "r")
poem = p.read()
if ("Twinkle" or "twinkle" in poem):
       print("The file contains the word Twinkle")
else: 
       print("The file does not contain the word Twinkle")
p.close()