class Student:
    def __init__(self, name, cpr):
        # Name is a string, no numbers are allowed in the string, and name should not be empty
        # Cpr format 'xxxxxx-xxxx' where x is numbers, and is a valid cpr number
        self.name = self.set_name(name)
        self.cpr = self.set_cpr(cpr)

    def set_name(self, name):
        if name == None:
            raise ValueError(None)
        elif type(name) != str:
            raise TypeError('You can not have a number name')
        else:
            for s in name:
                if s.isdigit():
                    raise ValueError('You have a number in your name?')
                    
        return name

    def set_cpr(self, cpr):
        return cpr


class Course:
    def __init__(self, title, course_id):
        # Title is a String
        # course id is in the right format
        # S19-PYT
        #    * S could also be F (Spring or Fall)
        #    * 19 is the year
        #    * PYT is the first 3 letters in the Course title
        self.title = title
        self.course_id = course_id

    def edit_title(self):
        pass

    def edit_course_id(self):
        pass


class Enrollment:
    def __init__(self, Student, Course):
        # Make sure the attributes are of the right type
        self.student = Student
        self.course = Course

    def grade_student(self, grade):
        # Grade the student,
        # if student already graded thats it,
        # it can not be changed
        self.grade = grade


if __name__ == "__main__":
    pass
