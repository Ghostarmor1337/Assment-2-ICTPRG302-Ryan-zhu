
#This Function allows the user to input they details and encrypt they paasword 
def add_details():
    Uname = input("\nEnter your username ")
    Pwrd = input("\nEnter your password ")
    website = input("\nEnter your website ")

    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    enPwrd = "".join([charSet[(charSet.find(c)+3)%95] for c in Pwrd])


    f = open("file.txt", "a")
    f.write(Uname + "   " + enPwrd + "   " + website + "   ")
    print("\nYour new details have now been stored\n")

#This function lets the user to view they file while automacticlly format it and dencrypting the password
def format_display():
    try:
        f = open('file.txt')  
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
        Pwrd = dataList [i+1]
        charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
        dePwrd = "".join([charSet[(charSet.find(c)-3)%95] for c in Pwrd])
        print(f"{border}{dataList[i] : ^20}{border}{dePwrd : ^20}{border}{dataList[i+2] : ^20}")   
        i += 3
    else:
        print("All data decrypted")

# Give the user some context.
print("\nDo you want view or store cedentuals …………………………")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    ''' Displays an Options Menu. You will need to update this code so that this section is replaced
    by the printing of a single global variable called 'menu' which has been assigned a multi line string that contains your 
    options menu. You will need to declare the variable in the same place as the 'choice' variable'''
    
    print("[1] Add stored cedentuals")
    print("[2] View stored cedentuals……")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice ")
    
    # Respond to the user's choice. You will need to ammend this section to reflect the menu requirements of the assessment
    if choice == '1':
        add_details()
        print("\noption 1 slected\n")
    elif choice == '2':
        format_display()
        print("\noption 2 slected…….\n")
    elif choice == 'q':
        print("\nquit program\n")
    else:
        print("\nInvalid option, please try again.\n")
        
# Print a message that we are all finished.
print("Program exit.")
