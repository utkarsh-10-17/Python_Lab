class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

class StudentInformationSystem:
    def __init__(self):
        self.students = {}

    def add_student_details(self, roll_number, name, age, grade):
        if roll_number not in self.students:
            new_student = Student(roll_number, name, age, grade)
            self.students[roll_number] = new_student
            print("Student added successfully.")
        else:
            print("Roll Number already exists. Try a different Roll Number.")

    def search_student(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            print(f"Roll Number: {student.roll_number}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
        else:
            print("Roll Number does not exist.")

    def display_all_students(self):
        if self.students:
            print("Student Information:")
            for roll_number, student in self.students.items():
                print(f"Roll Number: {student.roll_number}")
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Grade: {student.grade}")
                print("---------------------")
        else:
            print("No student information available.")

# Main function to run the program
def main():
    sis = StudentInformationSystem()

    while True:
        print("\nStudent Information System")
        print("1. Add Student Details")
        print("2. Search for Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            sis.add_student_details(roll, name, age, grade)
        elif choice == '2':
            roll = input("Enter Roll Number to search: ")
            sis.search_student(roll)
        elif choice == '3':
            sis.display_all_students()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
