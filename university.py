class University:
    def __init__(self, name, address, id):
        self.name = name
        self.address = address
        self.id = id
        self.departments = []

    def create_department(self, name, id, faculty_id):
        from department import Department
        dept = Department(name, id, faculty_id)
        self.departments.append(dept)
        return dept

    def remove_department(self, id):
        for dept in self.departments:
            if dept.id == id:
                # First remove all courses from professors
                for prof in dept.professors:
                    prof.courses.clear()
                # Then remove professors
                dept.professors.clear()
                # Finally remove the department
                self.departments.remove(dept)
                return True
        return False

    def list_departments(self):
        return self.departments