class Course(object):
    def __init__(self, coursename, coursenum, section, term_year, numofstudents): #constructor for course
        self.coursename = coursename #attributes for course
        self.coursenum = coursenum
        self.section = section
        self.term_year = term_year
        self.numofstudents = numofstudents

    def change_coursename(self, new_coursename): #allows you to change name of course
        self.coursename = new_coursename

    def change_coursenum(self, new_coursenum): #allows you to change course number
        self.coursenum = new_coursenum

    def change_section(self, new_section): #allows you to change course section
        self.section = new_section

    def change_term_year(self, new_term_year): # allows you to change year and term
        self.term_year = new_term_year

    def change_numofstudents(self, new_numofstudents): # allows you to change num of students
        self.numofstudents = new_numofstudents

    def display_course_info(self): # displays each attribute
        print(f"Course Name: {self.coursename}")
        print(f"Course Number: {self.coursenum}")
        print(f"Section: {self.section}")
        print(f"Term and Year: {self.term_year}")
        print(f"Number of Students: {self.numofstudents}")
        print()


def main():
    num_courses = int(input("How many courses do you want to create? ")) #prompts user input
    course_array = []

    for _ in range(num_courses): #display value for each attribute
        coursename = input("Enter Course Name: ")
        coursenum = input("Enter Course Number: ")
        section = input("Enter Section: ")
        term_year = input("Enter Term and Year: ")
        numofstudents = input("Enter Number of Students: ")

        course = Course(coursename, coursenum, section, term_year, numofstudents)

        # Change the value of one attribute 
        new_coursename = input("Enter the new course name: ")
        course.change_coursename(new_coursename)

        course_array.append(course)

    print("\nCourse Information:")
    for course in course_array:
        course.display_course_info()


if __name__ == "__main__":
    main()