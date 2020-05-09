# password manager


def readPassword():
    # get the name of the password
    # serviceFile = open("serviceFile.txt", "r")
    # passToFind = input("Which password do you want to obtain?")


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
        serviceFile.write(serviceName)
        # saves the password in the other file
        passwordFile.write(passwordValue1)
        # resets variables to empty strings
        passwordValue1 = ''
        passwrodValue2 = ''
        # close both files
        serviceFile.close()
        passwordFile.close()
        # print success message
        print("Password successfully stored")
    else:
        # irregular path: starts over
        serviceFile.close()
        passwordFile.close()
        savePassword()


def deletePassword():
    # get name of the password
    print("delet")

# password access - only called if the user passes the getPassword function.


def accessPasswords():
    userInput = input(
        "Would you like to store (s) a password, read (r) a password, or remove (d) a password from the system?")
    if (userInput == "s"):
        savePassword()
    elif(userInput == "r"):
        readPassword()
    elif(userInput == "d"):
        deletePassword()
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
