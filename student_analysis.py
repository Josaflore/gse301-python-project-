#Data structures

department_info = ("Religion Department", "Faculty of Technology", 2025)

students = []
student_names = []
unique_courses = set()
#set of students who passed python
set_pass = set()
#set of students with cgpa > 4.0
set_merit = set()




#Function for new student


def add_new_student():
            print("\nAdd new student")
            name = input("Student name: ")
            matric = input("Matricule number: ")
            age, cgpa = validation()
            #variable to check if student failed course
            outstanding = False
            is_active = False
            if (cgpa > 4.0):
                set_merit.add(name)

            if age is None:
              return

            active_check = input("Is student active? (yes,y/no,n): ") 
            if active_check.lower() == "yes" or active_check.lower() == "y":
                is_active = True

            courses = input("Enter student courses separated by comma(e.g course1,course2,...):  ").split(",")
            courses = [course.strip() for course in courses]

            grades = {}
            for course in courses:
                score = int(input(f"Enter score for {course}: "))
                if score < 40:
                    #score less than 40 is fail (F) hence cannot graduate
                    outstanding = True
                if course.lower() == "physics":
                    if score > 49:
                        set_pass.add(name)
		   
                grades[course] = grader(score)

            student = {
		"name": name,
		"matric": matric,
		"age": age,
		"cgpa": cgpa,
		"is_active": is_active,
		"courses": courses,
                "outstanding": outstanding,
		"grades": grades
	    }

            students.append(student)
            student_names.append(name)
            unique_courses.update(courses)


# Grading Function

def grader(score):
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    match grade:
        case "A":
            print("Excellent performance")
        case "B":
            print("Very good performance")
        case "C":
            print("Good performance")
        case "D":
            print("Fair performance")
        case "E":
            print("Pass")
        case "F":
            print("Fail")

    return grade

# Type conversion and validation

def validation():
    try:
        age = int(input("Enter age: "))
        cgpa = float(input("Enter CGPA: "))

        if age < 16 or age > 40:
            raise ValueError("Age must be between 16 and 40")

        if cgpa < 0.0 or cgpa > 5.0:
            raise ValueError("CGPA must be between 0.0 and 5.0")

        return age, cgpa

    except ValueError as e:
        print("Invalid input:", e)
        return None, None

def check_graduation_eligibility(student):
#student eligible if cgpa >= 2.5 and they failed no course
    if student["cgpa"] >= 2.5 and student["is_active"] and not student["outstanding"]:
        return True, "Student is eligible for graduation"
    else:
        return False, "Student is NOT eligible for graduation"

def find_top_performer():
    return max(students, key=lambda s: s["cgpa"])

def view_students():
    for student in students:
        print(student)
        print(student["is_active"])


# List op and slicing
def analysis():
	assignment_scores = []
	print("\nEnter 10 assignment scores")

	for i in range(10):
	    score = int(input(f"Score {i + 1}: "))
	    assignment_scores.append(score)
        
        #getting scores 1,2 and 3
	top_3_scores = assignment_scores[:3]
        #getting last 5 scores in list
	last_5_scores = assignment_scores[-5:]
        #getting scores with step 2 ie score 1,3,5,7,9
	every_other_score = assignment_scores[::2]

	print("Top 3 scores:", top_3_scores)
	print("Last 5 scores:", last_5_scores)
	print("Every other score:", every_other_score)

# Set Operations
def set_operation():
	passed_and_merit = set_pass & set_merit
	all_students = set_pass | set_merit
	passed_not_merit = set_pass - set_merit

	print("Passed and merit:", passed_and_merit)
	print("All students:", all_students)
	print("Passed but not merit:", passed_not_merit)



def menu():
    while True:
        print("\n1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Analysis and reporting")
        print("6. Set Operations")	
        print("7. Exit")

        choice = input("Select option: ")

        match choice:
            case "1":
                view_students()
            case "2":
                add_new_student()
            case "3":
                name = input("Enter student name: ")
                for student in students:
                    if student["name"] == name:
                        status, message = check_graduation_eligibility(student)
                        print(message)
                        break
                else:
                    print("Student not found")
            case "4":
                top = find_top_performer()
                print("Top performer:", top["name"], "CGPA:", top["cgpa"])
            case "5":
                analysis()
            case "6":
                set_operation()
            case "7":
                print("Exiting system")
                break
            case _:
                print("Invalid choice")

menu()

