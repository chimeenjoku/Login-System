"""
Created on  Nov 5 2017

@author: Chime Njoku
"""


#Implementation of a User Login System


accounts = {}


def welcomeMenu():
    mode= ""
    while mode != "q":
        mode = input("\nAre you a registered user? y/n or press q to quit:  \n")
        if mode == 'y':
            oldUser()
        elif mode == 'n':
            createUser()

def createUser():
    createLogin = input("Create Username:")

    if createLogin in accounts:
        print("\n!Username already exists!\n")
    else:
        createPassw = input("Create password: ")
        confirmPassw = input("Confirm password: ")
        while createPassw != confirmPassw:
            print("\n!Passwords do not match!\n")
            createPassw = input("Create password: ")
            confirmPassw = input("Confirm password: ") 
        accounts[createLogin] = createPassw
        print("\nYour account has been created!\n")
              

def oldUser():
        login = input("Enter Username: ")
        passw = input("Enter Password: ")

        if login in accounts and accounts[login] == passw:
              #Next implement three attempts to get the password correct and
              #is to make the user access something by calling another function or
              #dictionary in some way
              print("\nLogin successful!\n")
        elif login in accounts:
              print("\n!Wrong password!\n")
        else:
              print("\n!Account does not exist!\n")

welcomeMenu()
    
#end

    
