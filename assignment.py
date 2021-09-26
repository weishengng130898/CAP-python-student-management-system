def menu():
    print("")
    print("-----------------------------------")
    print ("1: Add New Student Data")
    print ("2. Modify Existing Student Data")
    print ("3. Search for specific Record")
    print ("4. Print specific Records")
    print ("5. Exit")
    print("-----------------------------------")
    option = 0
    inputOptionStatus = False

    while (inputOptionStatus == False):

        option = input("Please input option no: ")

        if (option == 1):
            inputOptionStatus = True
            addNewStudent()
        elif (option == 2):
            inputOptionStatus = True
            modifyStudentData()
        elif (option == 3):
            inputOptionStatus = True
            searchStudent()
        elif (option == 4):
            inputOptionStatus = True
            printInfo()
        elif (option == 5):
            inputOptionStatus = True
            break 
        else:
            print ("Unvalid option, please enter again")

def addNewStudent():
    print("")
    studentName = ""
    studentID = ""
    result = False

    while (True):
        


    

def modifyStudentData():
    print("")
    

def searchStudent():
    print("")

def printInfo():
    print("")

def programStart():
    menu()

def main():
    programStart()

if __name__ == "__main__":
    main()
