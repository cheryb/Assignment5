import sqlite3
database = sqlite3.connect("assignment5.db")
cursor = database.cursor()

# 4 • Log-in, log-out (all users). ##### DONE #########

def log_in_log_out():
    print("You have selected option 4. Log-in, log-out (all users).")
    choice = input("Are you a student, instructor or admin? ")
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



 

