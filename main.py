import os
from Modules.system import System

def main():
    system = System()
    if system.adminSignIn():
        initiate(system)
        print("Thank You For Using My Library Management System")

def initiate(system):
    while (True):
        os.system("clear")
        option = displayUserManual()
        match option:
            case '1':
                system.operateAdmin()
            case '2':
                system.operateBorrower()
            case '3':
                break
            case _ :
                print("Invalid input")

def displayUserManual():
    return input("Use Library as:\n1- Admin\n2- Borrower\n3- Exit\nChoice(1 or 2 or 3): ")

if __name__ == "__main__":
    main()