class Course:
    def __init__(self, name, id, professor_id):
        self.name = name
        self.id = id
        self.professor_id = professor_id
    
    def list_professors(self):
        return [self.professor_id]