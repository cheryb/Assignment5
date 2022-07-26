import sqlite3
import collections

# cursor.execute("""INSERT INTO STUDENT VALUES(10011, 'NITIN', 'BOHRA', 2022, 'BSCO', 'BOHRAN@WIT.EDU');""")
# cursor.execute("""INSERT INTO STUDENT VALUES(10012, 'JOHN', 'SMITH', 2022, 'BSEE', 'SMITHJ@WIT.EDU');""")

# cursor.execute("""DELETE FROM INSTRUCTOR WHERE name = 'Katie';""")

# cursor.execute("""UPDATE ADMIN SET TITLE = 'Vice President' WHERE NAME = 'Vera' AND SURNAME = 'Rubin';""")

#COURSE
# sql_command = """CREATE TABLE COURSE (
# CRN INT PRIMARY KEY NOT NULL,
# TITLE TEXT NOT NULL,
# DEPARTMENT TEXT NOT NULL,
# TIME INT NOT NULL,
# DAY TEXT NOT NULL,
# SEMESTER TEXT NOT NULL,
# YEAR INT NOT NULL,
# CREDITS INT NOT NULL);"""
# cursor.execute(sql_command)


# cursor.execute("""INSERT INTO COURSE VALUES(23230, 'CALCULUS 3', 'MATH', 1300, 'MW', 'SUMMER', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23231, 'ECONOMICS 2', 'HUSS', 1500, 'TF', 'SUMMER', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23233, 'JAVA PROGRAMMING', 'CS', 0900, 'MW', 'FALL', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23234, 'SENIOR DESIGN', 'ENGR', 1000, 'TF', 'SUMMER', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23235, 'BIOCHEMISTRY', 'BIO', 1200, 'MW', 'SPRING', 2022, 4);""")

# cursor.execute("""INSERT INTO COURSE VALUES(23236, 'ANALOG CIRCUIT DESIGN', 'BSCO', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23237, 'POWER SYSTEMS', 'BSEE', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23238, 'ARCH DESIGN', 'BSAS', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23239, 'ALGORITHMS', 'BCOS', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23240, 'CAD/CAM', 'BSME', 1200, 'MW', 'SPRING', 2022, 4);""")

# cursor.execute("""INSERT INTO COURSE VALUES(23241, 'ROBOTICS AND PARTS', 'BSME', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23242, 'EMBEDDED SYSTEMS', 'BSEE', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23243, 'SIGNAL AND SYSTEMS', 'BSCO', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23244, 'INTERIOR DESIGN', 'BSAS', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23245, 'SOCIOLOGY', 'HUSS', 1200, 'MW', 'SPRING', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES(23246, 'PSYCHOLOGY', 'HUSS', 1200, 'MW', 'SPRING', 2022, 4);""")

# query from the database
# cursor.execute("""SELECT * FROM STUDENT WHERE MAJOR = 'BSCO'""")
# query_result = cursor.fetchall()
# print(query_result)

# cursor.execute("""SELECT * FROM ADMIN WHERE TITLE = 'President'""")
# query_result = cursor.fetchall()
# print(query_result)

# cursor.execute("""SELECT * FROM INSTRUCTOR WHERE HIREYEAR >= 1940""")
# query_result = cursor.fetchall()
# print(query_result)


# cursor.execute("""SELECT TITLE, DEPARTMENT FROM COURSE""")
# course_list = cursor.fetchall()
# # print(course_list)

# cursor.execute("""SELECT NAME, SURNAME, DEPT FROM INSTRUCTOR""")
# instructor_list = cursor.fetchall()
# # print(instructor_list)

# result = collections.defaultdict(list)
# for instructor in instructor_list:
#     name = instructor[0]
#     surname = instructor[1]
#     instructor_dept = instructor[2]
#     for course in course_list:
#         course_name = course[0]
#         course_dept = course[1]
#         if instructor_dept == course_dept:
#             result[name+surname].append(course_name)

# for instructor, courses in result.items():
#     print(instructor, "-", courses)


'''
• Add/remove course from semester schedule (based on course ID number).
• Assemble and print course roster (instructor).
• Add/remove courses from the system (admin).
• Log-in, log-out (all users).
• Search all courses (all users) .
• Search courses based on parameters (all users).
• A menu to implement the use-cases.
• Edit classes as necessary to reflect the class diagrams.
'''


database = sqlite3.connect("assignment5.db")
cursor = database.cursor()

# 1 • Add/remove course from semester schedule (based on course ID number).

def add_remove_course_from_schedule():
    print("You have selected option 1. Add/remove course from semester schedule (based on course ID number).")

# 2 • Assemble and print course roster (instructor).

def print_course():
    print("You have selected option 2. Assemble and print course roster (instructor).")

# 3 • Add/remove courses from the system (admin).

def add_remove_course_from_system():
    print("You have selected option 3. Add/remove courses from the system (admin).")
    cursor.execute("""INSERT INTO COURSE VALUES(23300, 'DATA STRUCTURES', 'BSCS', 1400, 'MW', 'SPRING', 2022, 4);""")
    cursor.execute("""DELETE FROM COURSE WHERE title = 'CALCULUS 3';""")

# 4 • Log-in, log-out (all users).

def log_in_log_out():
    print("You have selected option 4. Log-in, log-out (all users).")

# 5 • Search all courses (all users) .

def search_all_courses():
    print("You have selected option 5. Search all courses (all users).")

    cursor.execute("""SELECT title FROM COURSE""")
    course_list = cursor.fetchall()
    for c in course_list:
        print(c)

# 6 • Search courses based on parameters (all users).

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

# 7 • A menu to implement the use-cases.

user_input = input("Please select an option \n 1. Add/remove course from semester schedule (based on course ID number). \n 2. Assemble and print course roster (instructor). \n 3. Add/remove courses from the system (admin). \n 4. Log-in, log-out (all users). \n 5. Search all courses (all users). \n 6. Search courses based on parameters (all users).: \n")
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

