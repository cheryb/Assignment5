import sqlite3
database = sqlite3.connect("assignment5.db")
cursor = database.cursor()

# 1 • Add/remove course from semester schedule (based on course ID number).

def add_remove_course_from_schedule():
    print("You have selected option 1. Add/remove course from semester schedule (based on course ID number).")
    choice2 = input("Do you want to add (1) or remove(2) this course from your schedule: ")
    while choice2 == 1 or 2:
       
        choice2 = int(choice2)
        if choice2 == 1:

            course = input("Enter course ID number: ")
            course = int(course)
            cursor.execute("""SELECT crn FROM COURSE WHERE crn=?""", [course])
            for row in iter(cursor.fetchone, None):
                print(row)
                
        elif choice2 == 2:
            course = input("Enter course ID number: ")
            course = int(course)
            cursor.execute("""SELECT crn FROM COURSE WHERE crn=?""", [course])
            for row in iter(cursor.fetchone, None):
                print(row)
                

# 2 • Assemble and print course roster (instructor).
def print_course():
    print("You have selected option 2. Assemble and print course roster (instructor).")

# 3 • Add/remove courses from the system (admin). ##### DONE #########

def add_remove_course_from_system():
    print("You have selected option 3. Add/remove courses from the system (admin).")
    cursor.execute("""INSERT INTO COURSE VALUES(23300, 'DATA STRUCTURES', 'BSCS', 1400, 'MW', 'SPRING', 2022, 4);""")
    cursor.execute("""DELETE FROM COURSE WHERE title = 'CALCULUS 3';""")

# 4 • Log-in, log-out (all users).
def log_in_log_out():
    print("You have selected option 4. Log-in, log-out (all users).")
    choice = input("Are you a student (1), instructor(2) or admin(3)? ")
    choice = int(choice) 
    name = input("Enter email: ")
    if choice == 1:
        cursor.execute("""SELECT email FROM STUDENT WHERE email=?""", [name])
        for row in iter(cursor.fetchone, None):
            print(row)
            print("You are now logged in")
    elif choice == 2:
        cursor.execute("""SELECT email FROM INSTRUCTOR WHERE email=?""", [name])
        for row in iter(cursor.fetchone, None):
            print(row)
            print("You are now logged in")
    elif choice == 3:
        cursor.execute("""SELECT email FROM ADMIN WHERE email=?""", [name])
        for row in iter(cursor.fetchone, None):
            print(row)
            print("You are now logged in")



 
    
# 5 • Search all courses (all users) . ###### DONE #########

def search_all_courses():
    print("You have selected option 5. Search all courses (all users).")

    cursor.execute("""SELECT title FROM COURSE""")
    course_list = cursor.fetchall()
    for c in course_list:
        print(c)

# 6 • Search courses based on parameters (all users). ######## DONE #########

def search_specific_courses():
    print("You have selected option 6. Search courses based on parameters (all users).")

    parameters = ['CRN', 'TITLE', 'DEPARTMENT', 'TIME', 'DAY', 'SEMESTER']
    inputs = [''] * 6
    for i in range(6):
        parameter = parameters[i]
        inputs[i] = input(f'Enter a {parameter}: ')

    crn, title, department, time, day, semester = inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]
    cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%s' OR TITLE = '%s' OR DEPARTMENT = '%s' OR TIME = '%s' OR DAY = '%s' OR SEMESTER = '%s';""" % (crn, title, department, time, day, semester)) 

    course_list = cursor.fetchall()
    for c in course_list:
        print(c)

# 7 • A menu to implement the use-cases. ######## DONE #######

user_input = input("Please select an option \n 1. Add/remove course from semester schedule (based on course ID number). \n 2. Assemble and print course roster (instructor). \n 3. Add/remove courses from the system (admin). \n 4. Log-in, log-out (all users). \n 5. Search all courses (all users). \n 6. Search courses based on parameters (all users): \n")
user_input = int(user_input)

if user_input == 1:
    add_remove_course_from_schedule()
elif user_input == 2:
    print_course()
elif user_input == 3:
    add_remove_course_from_system()
elif user_input == 4:
    log_in_log_out()
elif user_input == 5:
    search_all_courses()
elif user_input == 6:
    search_specific_courses()
database.commit()
database.close()

