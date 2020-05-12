# password manager
import secrets


def generateKey():
    # Generate a couple random numbers and save them on different lines
    keyFile = open("key.txt", "a")
    loopHelper = 0
    while(loopHelper < 5):
        keyFile.write(str(secrets.randbelow(7)) + '\n')
        loopHelper += 1


def encryptData():
    # Open files
    keyFile = open("key.txt", "r")
    passFile = open("passwordFile.txt", "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        print("Duplicating data...")
        # Saves the unencrypted password file
        passArray = []
        for line in passFile:
            currentLine = line.strip()
            passArray.append(currentLine)
        print("Encrypting data...")
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
        print("Saving data...")
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
        print("Saved data")
    else:
        # No key, so generate one
        generateKey()
        encryptData()


def decryptData():
    # Open files
    keyFile = open("key.txt", "r")
    passFile = open("passwordFile.txt", "r")
    if(keyFile.read() != ''):
        keyFile.close()
        # Nomial path:
        print("Duplicating data...")
        # Saves the unencrypted password file
        passArray = []
        for line in passFile:
            currentLine = line.strip()
            passArray.append(currentLine)
        print("Decrypting data...")
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
        print("Saving data...")
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


def readPassword():
    # get the name of the password
    serviceFile = open("serviceFile.txt", "r")
    passwordFile = open("passwordFile.txt", "r")
    servToFind = input("Which password do you want to obtain?")
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
            print(passwordList[serviceListCap])
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
        "Would you like to store (s) a password, read (r) a password, or quit (q) the program?")
    if (userInput == "s"):
        savePassword()
    elif(userInput == "r"):
        readPassword()
    elif(userInput == "q"):
        encryptData()
        quit()
    else:
        print("Please enter either s, r, or q")
    accessPasswords()


# password protection


def getPassword():

    # open file containing master password
    decryptData()
    masterPasswordFile = open(
        "masterPassword.txt", "r")
    # saves the password temporarily
    masterPass = masterPasswordFile.read()
    masterPasswordFile.close()
    # check if the password file is empty
    if (masterPass != ''):
        # if the master password is not empty, get user to input the master password
        masterPassInput = input("Enter your master password:")
        # if the entered password matches the password in the master
        if (masterPassInput == masterPass):
            # begin the normal program
            accessPasswords()
        else:
            # tell user that their password is incorrect
            print("Password incorrect")
            # go back to the start of the getPassword function
            getPassword()
    else:
        # password does not exist, so create a password
        # open the password file up in write mode
        masterPasswordFile = open(
            "masterPassword.txt", "w")
        # get the user to input their password 2x for security
        newPass1 = input("What would you like your password to be?\n")
        newPass2 = input("Confirm your password:")
        # check if the password is the same both times
        if(newPass1 == newPass2):
            # save the new password in the file
            masterPasswordFile.write(newPass1)
            masterPasswordFile.close()
            # begin the program
            accessPasswords()
        else:
            # if the passwords do not match, inform the user and have the user start over.
            print("The passwords do not match")
            encryptData()
            getPassword()


# start the program with the getPassword function
getPassword()
