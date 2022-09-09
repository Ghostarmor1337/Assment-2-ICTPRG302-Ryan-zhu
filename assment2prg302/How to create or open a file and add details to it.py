Uname = input("\nEnter your username ")
Pwrd = input("\nEnter your password ")
website = input("\nEnter your website ")

charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
enPward = "".join([charSet[(charSet.find(c)+3)%95] for c in Pwrd])


f = open("file.txt", "a")
f.write(Uname + "   " + enPward + "   " + website + "   ")
print("\nYour new details have now been stored\n")