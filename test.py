def add_remove_course_from_schedule():
    print("You have selected option 1. Add/remove course from semester schedule (based on course ID number).")

def print_course():
    print("You have selected option 2. Assemble and print course roster (instructor).")

def add_remove_course_from_system():
    print("You have selected option 3. Add/remove courses from the system (admin).")

def log_in_log_out():
    print("You have selected option 4. Log-in, log-out (all users).")

def search_all_courses():
    print("You have selected option 5. Search all courses (all users).")

def search_specific_courses():
    print("You have selected option 6. Search courses based on parameters (all users).")


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

