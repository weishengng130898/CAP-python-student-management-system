import datetime

def mainMenu():
    print("")
    print("-----------------------------------")
    print ("1: Add New Student Data")
    print ("2. Modify Existing Student Data")
    print ("3. Search for specific Record")
    print ("4. Print specific Records")
    print ("5. Exit")
    print("-----------------------------------")
    print("\n")

def menu():
    option = 0
    inputOptionStatus = False
    while (inputOptionStatus == False):
        mainMenu()
        option = input("Please input option no: ")
        if (option == "1"):
            addNewStudent()
        elif (option == "2"):
            modifyStudentData()
        elif (option == "3"):
            searchStudent()
        elif (option == "4"):
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

def checkStudentExist(id):
    flag = False
    if(len(studentData)>0):
        for x in studentData:
            if(str(id) == str(x[0])):
                flag = True
    return flag

def getStudentId():
    while (True):
        print("Please enter student id, 'X' to exit")
        idExistStatus = False
        studentId = input()
        idExistStatus = checkStudentExist(studentId)
        
        if (studentId.upper() == "X"):
            return studentId 
        elif (studentId.replace(" ","") == "" or not studentId.isdigit()):
            print("Student name cannot be empty and must be digit")
        else:
            if(idExistStatus == True):
                option = ""
                while (not option == "" or not option.upper() == 'R' or not option.upper() == 'X'):
                    print("Student id exist, Press X to exit, R to reenter")
                    option = input()
                    if(str(option.upper()) == 'R'):
                        break
                    elif(str(option.upper()) == 'X'):
                        return None
                    else:
                        print("Error, Invalid option")
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
        print("Please enter date of birth (digit only), 'X' to exit\n")
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
            studentDateOfBirth = datetime.date(int(dateOfBirthYear), int(dateOfBirthMonth), int(dateOfBirthDay))
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
            studentDateOfRegistrationYear = datetime.date(int(dateOfRegistrationYear), int(dateOfRegistrationMonth), int(dateOfRegistrationDay))
            return studentDateOfRegistrationYear

def getStrDateFormat(date):
    dateStr = date.strftime("%d")
    monthStr = date.strftime("%m")
    yearStr = date.strftime("%Y")
    return dateStr + "/" + monthStr + "/" + yearStr
    
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
        course = input()
        if(not course.upper() == 'X'):
            courseValid = checkCourseValid(course)
            if(courseValid == True):
                return course
            else:
                print("Error, Unvalid course")
        else:
            return course


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
                        dateOfBirth = getStrDateFormat(studentDateOfBirth)
                        registrationDate = getStrDateFormat(studentDateOfRegistrationYear)
                        studentData.append([studentId, studentName, dateOfBirth, 
                                            registrationDate, studentCourse])
                        print("Record added successfully")

        print("Continue add another new record (Y/N)? ")
        option = input()

        if(option.upper() == 'N'):
            break
        elif(option.upper() == 'Y'):
            pass
        else:
            print("Student ID already exists, please try again")
            break

def modifyStudentData():
    print("")
    

def searchStudent():
    search_item = input("Search: ")
    searchCount = 0
    foundResults = []
    if not search_item:
        print("No input detected")
    else:
        print("Found search results: \n")
        if len(studentData) > 0:
            for x in studentData:
                j = 0
                for j in range(4):
                    if search_item in x[j]:
                        print(x)
                        searchCount = searchCount + 1
                    j = j + 1
            if searchCount == 0:
                print("No relevant results found")
        else:
            print("There is no data recorded")

def printInfo():
    num=1
    print("No. \t\tID \t\tName \t\tDate of birth \t\tRegistered date \t\tCourse")
    for x in studentData:
        print(num,"\t\t", x[0],"\t\t",x[1],"\t\t",x[2], "\t\t", x[3], "\t\t", x[4])
        num = num+1

def programStart():
    global courseDist
    courseDist = {'IT':'Information Technology', 'CS':'Computer Science', 'ME':'Mechanical Engineering'}
    global studentData
    # studentData = [["1","2"],["3","4"]] dummy
    studentData = []
    while (True):
        menu()

# main
def main():
    programStart()

if __name__ == "__main__":
    main()
    
