# password manager
import secrets


# sets up master password recovery


def recoverSetup():
    with open("recover.txt", "w") as file:
        que = input("What would you like your recovery question to be?")
        check = input("Are you sure? (enter \'y\' or \'n\')")
        if(check == "y"):
            file.write(que)
        elif(check == "n"):
            recoverSetup()
        else:
            recoverSetup()
        ans = input("What is the answer to your question?")
        checka = input("Are you sure? (enter \'y\' or \'n\')")
        if(checka == "y"):
            with open("serviceFile.txt", "a") as sfile:
                sfile.write("mrecovery" + '\n')
            with open("passwordFile.txt", "a") as pfile:
                pfile.write(ans + '\n')
        elif(checka == "n"):
            recoverSetup()
        else:
            print("please enter \'y\' or \'n\'.")
            recoverSetup()


# lists all services stored in the manager


def listServ():
    # list out all stored passwords
    servFile = open("serviceFile.txt", "r")
    for line in servFile:
        currentLine = line.strip()
        print(currentLine)


# generates a new key - called every time the program quits


def generateKey():
    # Generate a couple random numbers and save them on different lines
    keyFile = open("key.txt", "w")
    loopHelper = 0
    while(loopHelper < 5):
        keyFile.write(str(secrets.randbelow(7)) + '\n')
        loopHelper += 1
    print("Key exchanged")


# encrypts the data with the key in key.txt


def encryptData():
    # Open files
    keyFile = open("key.txt", "r")
    passFile = open("passwordFile.txt", "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted password file
        passArray = []
        for line in passFile:
            currentLine = line.strip()
            passArray.append(currentLine)
        passFile.close()
        passFile = open("passwordFile.txt", "w")
        passFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all 5 digits of the key
        with open("key.txt", "r") as keyFile:
            for line in keyFile:
                keyLine = line.strip()
                keyArray.append(keyLine)
        # for each line in the password file
        for element in passArray:
            # Reset/create a string which holds the current encrypted line
            encryptedLine = ''
            # For each character in each line of the password file
            for char in passArray[elemLoopHelper]:
                # Figure out which element of the key is being added
                polyAdd = int(keyArray[keySwitcher])
                # Go through key values and add them to each
                enChar = ord(char) + polyAdd
                # Convert enChar to enCharS
                enCharS = chr(enChar)
                # Add each newly encrypted character to the encryptedLine string
                encryptedLine += enCharS
                # Change the line being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == 5):
                    keySwitcher = 0
            passArray[elemLoopHelper] = encryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open("passwordFile.txt", "a") as pwf:
            for element in passArray:
                pwf.writelines(element + '\n')
        print("Encrypted data")
    else:
        # No key, so generate one
        generateKey()
        encryptData()


# decrypts the data with the same key used to encrypt the data


def decryptData():
    # Open files
    keyFile = open("key.txt", "r")
    passFile = open("passwordFile.txt", "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        # Saves the unencrypted password file
        passArray = []
        for line in passFile:
            currentLine = line.strip()
            passArray.append(currentLine)
        passFile.close()
        passFile = open("passwordFile.txt", "w")
        passFile.close()
        elemLoopHelper = 0
        keyArray = []
        keySwitcher = 0
        # Populate the keyArray with all 5 digits of the key
        with open("key.txt", "r") as keyFile:
            for line in keyFile:
                keyLine = line.strip()
                keyArray.append(keyLine)
        # for each line in the password file
        for element in passArray:
            # Reset/create a string which holds the current encrypted line
            decryptedLine = ''
            # For each character in each line of the password file
            for char in passArray[elemLoopHelper]:
                # Figure out which element of the key is being added
                polyAdd = int(keyArray[keySwitcher])
                # Go through key values and add them to each
                deChar = ord(char) - polyAdd
                # Convert enChar to enCharS
                deCharS = chr(deChar)
                # Add each newly encrypted character to the encryptedLine string
                decryptedLine += deCharS
                # Change the line being read by the polyNumAdd
                keySwitcher += 1
                if (keySwitcher == 5):
                    keySwitcher = 0
            passArray[elemLoopHelper] = decryptedLine
            # Change the slot of the array that is being encrypted
            elemLoopHelper += 1
        with open("passwordFile.txt", "a") as pwf:
            for element in passArray:
                pwf.writelines(element + '\n')
        print("Decrypted data")
    else:
        print("Key not detected")


# returns the password belonging to the service parameter - if none found, returns None


def readPassword(service):
    # get the name of the password
    serviceFile = open("serviceFile.txt", "r")
    passwordFile = open("passwordFile.txt", "r")
    servToFind = service
    # create a list to store all the services
    serviceList = []
    serviceListCap = 0
    # create a list to store all the passwords
    passwordList = []
    # assign each line of the file to a list
    for line in serviceFile:
        lines = line.strip()
        serviceList.append(lines)
        serviceListCap += 1
    # assign each line of the password file to a list
    for line in passwordFile:
        pLines = line.strip()
        passwordList.append(pLines)
    # while there are still slots left to check in the lists
    while (serviceListCap > 0):
        # decrement servicelistcap
        serviceListCap -= 1
        # if a slot of the list is the correct service
        if(serviceList[serviceListCap] == servToFind):
            # print out the equivilant in the password list
            return(passwordList[serviceListCap])
    serviceFile.close()
    passwordFile.close()


# save passwords in two seperate files


def savePassword():
    # open the files required
    serviceFile = open("serviceFile.txt", "a")
    passwordFile = open("passwordFile.txt", "a")
    # get the name and value of the password
    serviceName = input("What is the service?")
    passwordValue1 = input("What is your password?")
    passwordValue2 = input("Confirm your password:")
    if (passwordValue1 == passwordValue2):
        # nomial path: saves the service name in one file
        serviceFile.write(serviceName + '\n')
        print("saved service " + serviceName)
        # saves the password in the other file
        passwordFile.write(passwordValue1 + '\n')
        # resets variables to empty strings
        passwordValue1 = ''
        passwordValue2 = ''
        # close both files
        serviceFile.close()
        passwordFile.close()
        # print success message
        print("Password successfully stored")
    else:
        # irregular path: starts over
        print("Passwords do not match")
        serviceFile.close()
        passwordFile.close()
        savePassword()


# password access - only called if the user passes the getPassword function.


def accessPasswords():
    userInput = input(
        "Would you like to store (s) a password, read (r) a password, or quit (q) the program? type (help) for more information.")
    if (userInput == "s"):
        savePassword()
    elif(userInput == "r"):
        servToFindP = input("What password are you trying to retrieve?")
        print(readPassword(servToFindP))
    elif(userInput == "q"):
        generateKey()
        encryptData()
        quit()
    elif(userInput == "l"):
        listServ()
    elif(userInput == "recover"):
        encryptData()
        print("attempted to restore data")
    elif(userInput == "help"):
        print("help: to store a password, input \'s\'. to read a password, input \'r\'. to quit the program, input \'q\'. to list all passwords stored, type \'l\'. to restore data from force quits, input \'recover\'.")
    else:
        print("Please enter either s, r, q, or help.")
    accessPasswords()


# password protection


def getPassword():
    # open file containing master password
    decryptData()
    masterPass = readPassword("master")
    # check if the password file is empty
    if (masterPass != None):
        # if the master password is not empty, get user to input the master password
        masterPassInput = input("Enter your master password:")
        # if the entered password matches the password in the master
        if (masterPassInput == masterPass):
            # begin the normal program
            accessPasswords()
        elif(masterPassInput == "recover"):
            with open("recover.txt", "r") as rec:
                question = rec.read()
            answer = input(question)
            if(answer == readPassword("mrecovery")):
                print("Your master password is: " + readPassword("master"))
                encryptData()
                getPassword()
            else:
                print("Incorrect.")
                encryptData()
                getPassword()
        else:
            # tell user that their password is incorrect
            print(
                "Password incorrect. If you have forgotten your master password, type \'recover\'.")
            # go back to the start of the getPassword function
            encryptData()
            getPassword()
    else:
        # password does not exist, so create a password
        # open the password file up in write mode
        passwordFile = open(
            "passwordFile.txt", "w")
        servFile = open("serviceFile.txt", "w")
        # get the user to input their password 2x for security
        newPass1 = input("What would you like your password to be?\n")
        newPass2 = input("Confirm your password:")
        # check if the password is the same both times
        if(newPass1 == newPass2):
            # save the new password in the file
            servFile.write("master" + '\n')
            servFile.close()
            passwordFile.write(newPass1 + '\n')
            passwordFile.close()
            recoverSetup()
            # begin the program
            accessPasswords()
        else:
            # if the passwords do not match, inform the user and have the user start over.
            print("The passwords do not match")
            encryptData()
            getPassword()


# start the program with the getPassword function
getPassword()
