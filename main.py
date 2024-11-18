from universidade import Universidade as University


def display_summary(universities, current_univ):
    """Display a summary of the university system state."""
    print("\n=== SYSTEM SUMMARY ===")
    print(f"Total universities: {len(universities)}")

    if not current_univ:
        print("No university currently selected")
        print("=" * 25)
        return

    print(f"\nCurrent University: {current_univ.name} (ID: {current_univ.id})")
    print(f"Address: {current_univ.address}")

    if not current_univ.departments:
        print("\nNo departments registered")
        print("=" * 25)
        return

    print("\nDepartments:")
    for dept in current_univ.departments:
        print(f"- {dept.department_name} (ID: {dept.id})")

        if dept.professors:
            print("  Professors:")
            for prof in dept.professors:
                print(f"  * {prof.name} (ID: {prof.professor_id})")

                if prof.courses:
                    print("    Courses:")
                    for course in prof.courses:
                        print(f"    - {course.name} (ID: {course.id})")

    print("=" * 25)


def get_menu_choice():
    """Display menu options and get user choice."""
    menu_options = """
    University Management System
    ---------------------------
    1. Create university
    2. Remove university
    3. Create department
    4. Remove department
    5. List departments
    6. Add professor
    7. Remove professor
    8. List professors
    9. Add course
    10. Remove course
    11. List courses
    0. Exit
    """
    print(menu_options)
    return input("Choose an option: ")


def create_university():
    """Get university details from user input."""
    name = input("University name: ")
    address = input("University address: ")
    id_num = input("University ID: ")
    return name, address, id_num


def get_department_details():
    """Get department details from user input."""
    name = input("Department name: ")
    dept_id = int(input("Department ID: "))
    faculty_id = int(input("Faculty ID: "))
    return name, dept_id, faculty_id


def find_department(university, dept_id):
    """Find department by ID in the given university."""
    return next(
        (dept for dept in university.departments if dept.id == dept_id),
        None
    )


def find_professor(department, prof_id):
    """Find professor by ID in the given department."""
    return next(
        (prof for prof in department.professors if
         prof.professor_id == prof_id),
        None
    )


def handle_department_operations(university, choice):
    """Handle all department-related operations."""
    if not university:
        print("Please select or create a university first!")
        return

    if choice == "3":  # Create department
        name, dept_id, faculty_id = get_department_details()
        university.create_department(name, dept_id, faculty_id)
        print("Department created successfully!")

    elif choice == "4":  # Remove department
        dept_id = int(input("Department ID to remove: "))
        if university.remove_department(dept_id):
            print("Department removed successfully!")
        else:
            print("Department not found!")

    elif choice == "5":  # List departments
        departments = university.list_departments()
        if departments:
            print("\nDepartments:")
            for dept in departments:
                print(f"Name: {dept.department_name}, ID: {dept.id}")
        else:
            print("No departments registered!")


def handle_professor_operations(university, choice):
    """Handle all professor-related operations."""
    if not university.departments:
        print("Create a department first!")
        return

    dept_id = int(input("Department ID: "))
    department = find_department(university, dept_id)

    if not department:
        print("Department not found!")
        return

    if choice == "6":  # Add professor
        name = input("Professor name: ")
        prof_id = int(input("Professor ID: "))
        department.add_professor(name, prof_id)
        print("Professor added successfully!")

    elif choice == "7":  # Remove professor
        prof_id = int(input("Professor ID to remove: "))
        if department.delete_professor(prof_id):
            print("Professor removed successfully!")
        else:
            print("Professor not found!")

    elif choice == "8":  # List professors
        print("\nProfessors by Department:")
        found_any = False
        for dept in university.departments:
            professors = dept.list_professors()
            if professors:
                found_any = True
                print(f"\nDepartment: {dept.department_name}")
                for prof in professors:
                    print(f"Name: {prof.name}, ID: {prof.professor_id}")

        if not found_any:
            print("No professors registered in any department!")


def handle_course_operations(university, choice):
    """Handle all course-related operations."""
    if not university.departments:
        print("No departments registered!")
        return

    dept_id = int(input("Department ID: "))
    department = find_department(university, dept_id)

    if not department:
        print("Department not found!")
        return

    prof_id = int(input("Professor ID: "))
    professor = find_professor(department, prof_id)

    if not professor:
        print("Professor not found!")
        return

    if choice == "9":  # Add course
        name = input("Course name: ")
        course_id = int(input("Course ID: "))
        professor.add_course(name, course_id)
        print("Course added successfully!")

    elif choice == "10":  # Remove course
        course_id = int(input("Course ID to remove: "))
        if professor.delete_course(course_id):
            print("Course removed successfully!")
        else:
            print("Course not found!")

    elif choice == "11":  # List courses
        courses = professor.list_courses()
        if courses:
            print("\nCourses:")
            for course in courses:
                print(f"Name: {course.name}, ID: {course.id}")
        else:
            print("No courses registered for this professor!")


def main():
    """Main program loop."""
    universities = []
    current_univ = None

    while True:
        choice = get_menu_choice()

        if choice == "0":
            print("Exiting program...")
            break

        elif choice == "1":  # Create university
            name, address, id_num = create_university()
            current_univ = University(name, address, id_num)
            universities.append(current_univ)
            print("University created successfully!")

        elif choice == "2":  # Remove university
            if not universities:
                print("No universities registered!")
                continue

            id_to_remove = input("University ID to remove: ")
            for univ in universities:
                if univ.id == id_to_remove:
                    universities.remove(univ)
                    if univ == current_univ:
                        current_univ = None
                    print("University removed successfully!")
                    break
            else:
                print("University not found!")

        elif choice in ["3", "4", "5"]:
            handle_department_operations(current_univ, choice)

        elif choice in ["6", "7", "8"]:
            handle_professor_operations(current_univ, choice)

        elif choice in ["9", "10", "11"]:
            handle_course_operations(current_univ, choice)

        else:
            print("Invalid option!")

        if current_univ:
            display_summary(universities, current_univ)


if __name__ == "__main__":
    main()