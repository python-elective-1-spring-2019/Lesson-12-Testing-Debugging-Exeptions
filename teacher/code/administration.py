from school import *

# Create a list of all Courses
courses = [Course('Python', 'S19-PYT'), Course('Artificial Intelligence', 'S19-ART'), Course('Angular', 'S19-ANG')]

def add_course():
    title = input('Title for the Course: ')
    course_id = input('Course ID: ')
    courses.append(Course(title, course_id))

def remove_course():
    print(courses)
    course_id = input('What Course do you want to remove (Course ID): ')

    for c in courses:
        if course_id == c.course_id:
            courses.pop(c)

# Enroll Students to Courses
def enroll_students():
    pass

def remove_students():
    pass


def main():

    student = Student('1234')
    print('What would you like to do? ')
    print('Add course to course list (1)')
    print('Remove course from course list (2)')
    print('Enroll Student to enrollments list (3)')
    print('Remove Student from enrollments list (4)')
    inp = int(input())

    if inp == 1:
        add_course()
    elif inp == 2:
        pass
    elif inp == 3:
        pass
    elif inp == 4:
        pass

    print(courses)

if __name__ == "__main__":
    main()