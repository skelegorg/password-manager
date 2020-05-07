# password manager


def accessPasswords():

    # create a function called first in the manager


def initialize():
    masterPasswordFile = open("masterPasswordFile", "r")
    masterPass = masterPasswordFile.read()
    if (masterPass != ''):
        # if the master password is not empty, get user to input the master password
        masterPassInput = input("Enter your master password:")
        # if the entered password matches the password in the master
        if(masterPassInput == masterPass):
            # begin the normal program
        else:
            # tell user that their password is incorrect
            print("Password incorrect")
            # go back to the start of the initialize function
            initialize()
    else:
        # password does not exist, so create a password
        masterPasswordFile = open("masterPasswordFile", "w")
        newPass1 = input("What would you like your password to be?")
        newPass2 = input("Confirm your password:")
        # check if the password is the same both times
        if(newPass1 == newPass2):
            masterPasswordFile.write(newPass1)
        else:
            print("The passwords do not match")
        initialize()
