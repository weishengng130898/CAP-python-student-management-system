import datetime
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

        if (option == "1"):
            inputOptionStatus = True
            addNewStudent()
        elif (option == "2"):
            inputOptionStatus = True
            modifyStudentData()
        elif (option == "3"):
            inputOptionStatus = True
            searchStudent()
        elif (option == "4"):
            inputOptionStatus = True
            printInfo()
        elif (option == "5"):
            inputOptionStatus = True
            break 
        else:
            print ("Unvalid option, please enter again")

def getStudentName():
    studentName = ""

    while (True):
        print("Please enter student name, 'X' to exit")

        studentName = input()

        if (studentName == "X"):
            return studentName  
        elif (studentName.replace(" ","") == ""):
            print("Student name cannot be empty")
        else:
            return studentName       

def getStudentId():

    while (True):
        print("Please enter student id, 'X' to exit")

        studentId = input()

        if (studentId.upper() == "X"):
            return studentId 
        elif (studentId.replace(" ","") == "" or not studentId.isdigit()):
            print("Student name cannot be empty and must be digit")
        else:
            return studentId

def checkDateValid(year, month, day):
    correctDate = None
    try:
        date = datetime.datetime(int(year), int(month), int(day))
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate 

def getStudentDateOfBirth():
    while (True):
        dateValid = False
        print("Please enter date of birth (digit only), 'X' to exit")

        dateOfBirthYear = input("Year (YYYY): ")
        dateOfBirthMonth = input("Month (MM): ")
        dateOfBirthDay = input("Day: (DD): ")

        datevalid = checkDateValid(dateOfBirthYear, dateOfBirthMonth, dateOfBirthDay)
        if (dateOfBirthYear.upper() == "X" or dateOfBirthMonth.upper() == "X" or dateOfBirthDay.upper() == "X"):
            return studentDateOfBirth 
        elif (dateOfBirthYear.replace(" ","") == "" or dateOfBirthMonth.replace(" ","") == "" or dateOfBirthDay.replace(" ","") == ""):
            print("Student date of birth (Year, Month, Day) cannot be empty and must be valid date")       
        elif(datevalid == False):    
            print("Error, please enter valid date of birth")
        else:
            studentDateOfBirth = datetime.datetime(int(dateOfBirthYear), int(dateOfBirthMonth), int(dateOfBirthDay))
            return studentDateOfBirth

def getStudentDateOfRegistration():
    while (True):
        dateValid = False
        print("Please enter date of registration (digit only)")

        dateOfRegistrationYear = input("Year (YYYY): ")
        dateOfRegistrationMonth = input("Month (MM): ")
        dateOfRegistrationDay = input("Day: (DD): ")

        datevalid = checkDateValid(dateOfRegistrationYear, dateOfRegistrationMonth, dateOfRegistrationDay)
        if (dateOfRegistrationYear.upper() == "X" or dateOfRegistrationMonth.upper() == "X" or dateOfRegistrationDay.upper() == "X"):
            return dateOfRegistrationYear
        elif (dateOfRegistrationYear.replace(" ","") == "" or dateOfRegistrationMonth.replace(" ","") == "" or dateOfRegistrationDay.replace(" ","") == ""):
            print("Student date of registration  (Year, Month, Day) cannot be empty and must be valid date")
        elif(datevalid == False):    
            print("Error, please enter valid date of registration")
        else:
            studentDateOfRegistrationYear = datetime.datetime(int(dateOfRegistrationYear), int(dateOfRegistrationMonth), int(dateOfRegistrationDay))
            return dateOfRegistrationYear

def checkCourseValid(course):
    
    if (course.upper() in courseDist):
        return True
    else: 
        return False

def getStudentCourse():
    print("--------Course List----------------")
    for x in courseDist:
        print(x, ' - ', courseDist[x])
    print("-----------------------------------")

    courseValid = False
    while (True):
        print("Please enter student course, 'X' to exit")
        course = input ()

        if(not course.upper() == 'X'):
            courseValid = checkCourseValid(course)
            if(courseValid == True):
                return course
            else:
                print("Error, Unvalid course")
        else:
            return course

# def checkStudentExist():
#     exist = False
#     if(len(studentData)>0):

#     else

def addNewStudent():
    print("")
    studentName = ""
    studentID = None
    studentDateOfBirth = None
    studentDateOfRegistrationYear = None
    studentCourse = ""
    result = False

    while (True):
        studentId = getStudentId()
        if(not studentId == None and not studentId == 'X'):
            studentName = getStudentName()
            if(not studentName == "" and not studentName == 'X'):
                studentDateOfBirth = getStudentDateOfBirth()
                if(not studentDateOfBirth == None and not studentDateOfBirth == 'X'):
                    studentDateOfRegistrationYear = getStudentDateOfRegistration () 
                    if(not studentDateOfRegistrationYear == None and not studentDateOfRegistrationYear == 'X'):
                        studentCourse = getStudentCourse()
                        studentData.append([studentId, studentName, studentDateOfBirth, 
                                            studentDateOfRegistrationYear, studentCourse])
                        print("Record added successfully")

        option = input("Continue add another new record (Y/N)?")

        if(option == 'N'):
            break
        elif(option == 'Y'):
            pass
        else:
            print("Error, invalid option")

def modifyStudentData():
    print("")
    

def searchStudent():
    print("")

def printInfo():
    print("")

def programStart():
    global courseDist
    courseDist = {'IT':'Information Technology', 'CS':'Computer Science'}
    global studentData
    studentData = []
    menu()

def main():
    programStart()

if __name__ == "__main__":
    main()
    
