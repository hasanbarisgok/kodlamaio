class homework_1:
    students_list = ["Hasan Baris GOK", "John CENA","The ROCK"]
    
    def check_info_from_name():
        name = input("Please enter the student name + surname to see student info:")
        for i in range(len(homework_1.students_list)):
            if name == homework_1.students_list[i]:
                print(f"The student name is: {homework_1.students_list[i]}\nThe student number is: {i}")
                break
            else:
                print("The student is not member in school. Please check the student name again.")
                
    def check_info_from_student_no():
        student_no = int(input("Please enter the student school number."))
        print(f"The student name and surname are: {homework_1.students_list[student_no]}")            
                
    def add_student():
        name = input("Please enter the student name + surname for adding a student to database: ")
        homework_1.students_list.append(name)
        print(f"The student is added to database: {name}")
        
    def add_multiple_students():
        value = int(input("Please enter the value of how many students will add to database. Example:3\n Value: "))
        i = 1
        while i <= value:
            print(f"Enter the {i}. Student's info\n")
            homework_1.add_student()
            i += 1
    
    def remove_student():
        name = input("Please enter the student name + surname to remove student from database: ")
        if name in homework_1.students_list:
            homework_1.students_list.remove(name)
            print("New Student List:")
            for student in homework_1.students_list:
                print(student)
        else:
            print("The student is not member of the school. Please check the name again.")
                
                

instance = homework_1

instance.check_info_from_name()
instance.check_info_from_student_no()
instance.add_student()
instance.add_multiple_students()
instance.remove_student()
    
    
#@kodlama.io Python & Selenium Course Online.
