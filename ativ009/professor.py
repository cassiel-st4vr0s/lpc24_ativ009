class Professor:
    def __init__(self, name, professor_id, department_id):
        self.name = name
        self.professor_id = professor_id
        self.department_id = department_id
        self.courses = []
    
    def add_course(self, name, id):
        from ativ009.course import Course
        course = Course(name, id, self.professor_id)
        self.courses.append(course)
        return course
    
    def delete_course(self, id):
        for course in self.courses:
            if course.id == id:
                self.courses.remove(course)
                return True
        return False
    
    def list_courses(self):
        return self.courses