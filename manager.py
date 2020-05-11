# password manager
from cryptography.fernet import Fernet

# Generate a new key and encrypt the file with it


def encrypt():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyF:
        keyF.write(key)
    crypto_suite = Fernet(key)
    with open("passwordFile.txt", "rb") as passFile:
        plain = passFile.read()
    encrypted = crypto_suite.encrypt(plain)
    with open("passwordFile.txt", "wb") as encryptPass:
        encryptPass.write(encrypted)


def decrypt():
    with open("key.key", "rb") as keyFile:
        key = keyFile.read()
    crypto_suite = Fernet(key)
    with open("passwordFile.txt", "rb") as enPassFile:
        encrypted = enPassFile.read()
    plainText = crypto_suite.decrypt(encrypted)
    with open("passwordFile.txt", "wb") as dePassFile:
        dePassFile.write(plainText)


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
        quit()
    else:
        print("Please enter either s, r, or q")
    accessPasswords()


# password protection


def getPassword():
    # open file containing master password
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
            getPassword()


# start the program with the getPassword function

getPassword()
