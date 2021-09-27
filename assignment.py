import datetime

def mainMenuDisplay():
    print("")
    print("-----------------------------------")
    print ("1: Add New Student Data")
    print ("2. Modify Existing Student Data")
    print ("3. Search for specific Record")
    print ("4. Print specific Records")
    print ("5. Exit")
    print("-----------------------------------")
    print("\n")

def printCourseMenu():
    print("--------Course List----------------")
    for x in courseDist:
        print(x, ' - ', courseDist[x][0])
    print("-----------------------------------")

def printCourseDetails():
    print("----------------------Course List-----------------------")
    for x in courseDist:
        print("{:<6} {:<35} {:<12} {:<12}" .format("Course" , "Coourse Name" , "Min age" , "max age"))
        print("{:<6} {:<35} {:<12} {:<12}" .format(x  , courseDist[x][0] , courseDist[x][1] , courseDist[x][2]))
    print("--------------------------------------------------------")


def menu():
    option = 0
    run = True
    while (run == True):
        mainMenuDisplay()
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
            run = False
            return run 
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
        date = datetime.date(int(year), int(month), int(day))
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate 

def getStudentDateOfBirth():
    while (True):
        print("Please enter date of birth (digit only), 'X' to exit\n")
        dateOfBirthYear = input("Year (YYYY): ")
        dateOfBirthMonth = input("Month (MM): ")
        dateOfBirthDay = input("Day: (DD): ")
        datevalid = checkDateValid(dateOfBirthYear, dateOfBirthMonth, dateOfBirthDay)
        if (dateOfBirthYear.upper() == "X" or dateOfBirthMonth.upper() == "X" or dateOfBirthDay.upper() == "X"):
            return dateOfBirthYear 
        elif (dateOfBirthYear.replace(" ","") == "" or dateOfBirthMonth.replace(" ","") == "" or dateOfBirthDay.replace(" ","") == ""):
            print("Student date of birth (Year, Month, Day) cannot be empty and must be valid date")       
        elif(datevalid == False):    
            print("Error, please enter valid date of birth")
        else:
            studentDateOfBirth = datetime.date(int(dateOfBirthYear), int(dateOfBirthMonth), int(dateOfBirthDay))
            return studentDateOfBirth

def getStudentDateOfRegistration():
    while (True):
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
            studentDateOfRegistration = datetime.date(int(dateOfRegistrationYear), int(dateOfRegistrationMonth), int(dateOfRegistrationDay))
            return studentDateOfRegistration

def formatStrDateFormat(date):
    dateStr = date.strftime("%d")
    monthStr = date.strftime("%m")
    yearStr = date.strftime("%Y")
    return dateStr + "/" + monthStr + "/" + yearStr
    
def checkCourseValid(course):
    if (course.upper() in courseDist):
        return True
    else: 
        return False

def compareDates(dateOfBirth, registrationDate):
    validFlag = False
    if dateOfBirth < registrationDate:
        validFlag = True
    return validFlag

def getStudentCourse():
    printCourseDetails()
    courseValid = False
    while (True):
        print("Please enter student course(short form), 'X' to exit")
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
    studentId = None
    studentDateOfBirth = None
    studentDateOfRegistration = None
    studentCourse = ""
    isValid = False
    while (True):
        studentId = getStudentId()
        if(not studentId == None and not studentId == 'X'):
            studentName = getStudentName()
            if(not studentName == "" and not studentName == 'X'):
                studentDateOfBirth = getStudentDateOfBirth()
                if(not studentDateOfBirth == None and not studentDateOfBirth == 'X'):
                    studentDateOfRegistration = getStudentDateOfRegistration () 
                    if(not studentDateOfRegistration == None and not studentDateOfRegistration == 'X'):
                        isValid = compareDates(studentDateOfBirth,studentDateOfRegistration)
                        studentCourse = getStudentCourse().upper()
                        isValidAge = checkRegistrationDateIntervalValid(datetime.datetime.strptime(str(studentDateOfBirth), '%Y-%m-%d'),courseDist[studentCourse][1],courseDist[studentCourse][2])
                      
                        if(isValid == True):    
                            if (isValidAge == True):
                                dateOfBirth = formatStrDateFormat(studentDateOfBirth)
                                registrationDate = formatStrDateFormat(studentDateOfRegistration)
                                studentData.append([studentId, studentName, dateOfBirth, 
                                                registrationDate, studentCourse])
                                print("Record added successfully")
                        else:
                            print("Date of registration cannot be earlier than date of birth")
        if(isValid == True):
            option = ""
            while (not option.upper() == 'N' and not option.upper() == 'Y'):
                print("Continue add another new record Y = Yes/ N = No (Y/N)? ")
                option = input()
                if(option.upper() == 'N'):
                    option = 'N'
                elif(option.upper() == 'Y'):
                    pass
                else:
                    print("Error, invalid option")
            if(option.upper() == 'N'):
                break

def displayModificationMenu():
    print("-----------------------------------")
    print ("1: Name")
    print ("2. Course")
    print ("3. Date of Birth")
    print ("4. Date of Registration")
    print ("5. Exit")
    print("-----------------------------------")

def modifyNameWithId(id):
    newName = getStudentName()
    for x in studentData:
        if(str(id) == str(x[0])):
            x[1] = newName
        
def modifyCourseWithId(id):
    newCourse = getStudentCourse()
    for x in studentData:
        if(str(id) == str(x[0])):
            x[4] = newCourse

def modifyDateOfBirthWithId(id):
    newDateOfBirthWithId = getStudentDateOfBirth()
    newDateOfBirthWithId = getStudentDateOfBirth(newDateOfBirthWithId)
    for x in studentData:
        if(str(id) == str(x[0])):
            x[2] = newDateOfBirthWithId

def modifyDateOfRegistrationWithId(id):
    newDateOfBirthWithId = getStudentDateOfRegistration()
    newDateOfBirthWithId = formatStrDateFormat(newDateOfBirthWithId)
    for x in studentData:
        if(str(id) == str(x[0])):
            x[3] = newDateOfBirthWithId

def fromDobToAge(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def checkRegistrationDateIntervalValid(dob, minLimit, maxLimit):
    print(dob)
    age = fromDobToAge(dob)
    if (int(age) >= int(minLimit)):
        if (int(age) <= int(maxLimit)):
            return True
        else:
            print("Applicant does not meet the requirement for the program (age greater)")
    else:
        print("Applicant does not reach minimum age for the program")
        return False

def modifyStudentData():
    idExistStatus = False

    id = input("Please enter student id to modify: ")

    if(len(studentData)>0):
        
        idExistStatus = checkStudentExist(id)
        
        if(idExistStatus == True):
            
            for x in studentData:
                if(str(id) == str(x[0])):
                    for shorForm, item in courseDist.items():
                        if (str(x[4]) == shorForm):
                            fullCourseName = item[0]
                    print("Student details")
                    print("Student id: " + x[0])
                    print("Student name: " + x[1])
                    print("Student date of birth: " + x[2])
                    print("Student registration date: " + x[3])
                    print("Student course: " + x[4] + ' - ' + fullCourseName[0])

            displayModificationMenu()
            
            option = input("Please select element to modify: ") 

            if(option == "1"):
                modifyNameWithId(id)
            elif(option == "2"):
                modifyCourseWithId(id)
            elif(option == "3"):
                modifyDateOfBirthWithId(id)
            elif(option == "4"):
                modifyDateOfRegistrationWithId(id)
            else:
                print("Error, Please input the available option only")
            

        if(idExistStatus == False):
            print("Error student record id - " + id + " not found")
                
    else:
        print("No record found")

def searchStudent():
    search_item = input("Student id: ")
    if(search_item.replace(" ","") == ""):
        print("Empty input detected")
    searchCount = 0
    if not search_item:
        print("No input detected")
    else:
        if len(studentData) > 0:
            print("Found search results: \n")
            for x in studentData:
                if search_item in x[0]:
                    for shorForm, fullName in courseDist.items():
                        if (str(x[4]) == shorForm):
                            fullCourseName = fullName
                    print("Student details")
                    print("Student id: " + x[0])
                    print("Student name: " + x[1])
                    print("Student date of birth: " + x[2])
                    print("Student registration date: " + x[3])

                    print("Student course: " + x[4] + " - " + fullCourseName[0])
                    
                    searchCount = searchCount + 1
            if searchCount == 0:
                print("No relevant results found")
        else:
            print("There is no data recorded")

def printInfo():
    printCourseMenu()
    course = input("Course: ").upper()
    outputList = []

    if len(studentData) > 0:        
        for x in studentData:
            if not str(x[4]) in course:
                if course in str(courseDist.values()).upper(): 
                    outputList.append(x)
            else:
                outputList.append(x)
        if len(outputList) > 0:
            print ("{:<4} {:<25} {:<10} {:<10} {:<20}".format('id','name','DOB','reg. date', 'course'))
            for x in outputList:
                print ("{:<4} {:<25} {:<10} {:<10} {:<20}".format(x[0],x[1],x[2],x[3],x[4]))

    else:
        print("There is no data recorded")

def loadFromTextFileStudentData():
    pass

def writeToTextFileStudentData():
    pass

def programStart():
    global courseDist
    courseDist = {'IT':['Information Technology','18','21'], 'CS':['Computer Science','18','21'], 'ME':['Mechanical Engineering','20','22']}
    global studentData
    studentData = []
    runStatus = True
    while (runStatus == True):
        runStatus = menu()

# main
def main():
    programStart()

if __name__ == "__main__":
    main()
    
