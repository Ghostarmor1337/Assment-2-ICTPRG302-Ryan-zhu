try:
    f = open('file.txt')  
    print("file exists")
    f.close()    
except FileNotFoundError: # File not found exception
    print('No password file created, create and add data to a new file first')

f = open("file.txt", "r")
data = f.read() # 'data' now contains the contents of the file as a string
stripped_data = data.strip()
dataList = stripped_data.split("   ") # split string into a list with 3 spaces as the default delimiter
i = 0
border = "|"
print(f"{border}{'Userame' : ^20}{border}{'Password' : ^20}{border}{'Website' : ^20}")
print("--------------------------------------------------------------------")
while i < len(dataList): #repeat until 'i' is larger than the list length

    password = dataList [i+1]
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    denname = "".join([charSet[(charSet.find(c)-3)%95] for c in password])

     

    print(f"{border}{dataList[i] : ^20}{border}{dataList[i+1] : ^20}{border}{dataList[i+2] : ^20}")   
    i += 3
else:
    print("\nAll data has now been displayed\n")