class Department:
    def __init__(self, department_name, id, faculty_id):
        self.department_name = department_name
        self.id = id
        self.faculty_id = faculty_id
        self.professors = []

    def add_professor(self, name, professor_id):
        from ativ009.professor import Professor
        # Check if professor already exists
        if any(p.professor_id == professor_id for p in self.professors):
            return None
        prof = Professor(name, professor_id, self.id)
        self.professors.append(prof)
        return prof

    def delete_professor(self, professor_id):
        for prof in self.professors:
            if prof.professor_id == professor_id:
                # First remove all courses from professor
                prof.courses.clear()
                # Then remove the professor
                self.professors.remove(prof)
                return True
        return False

    def list_professors(self):
        return self.professors