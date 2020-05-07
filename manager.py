# password manager

# password access - only called if the user passes the getPassword function.


def accessPasswords():
    # for testing purposes
    print("hello, world!")

# password protection


def getPassword():
    # open file containing master password
    masterPasswordFile = open(
        "C:\Program Files\password-manager\masterPassword.txt", "r")
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
        masterPasswordFile = open("masterPasswordFile", "w")
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
