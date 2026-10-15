import os

with open("Students_Record","w") as f:
    f.write("___Students record____\n")
    f.close()
    
    
def add_students():
    Name= str(input("Enter the students name :"))
    Roll_no= int(input("Enter the students Roll_No :"))
    Python=int(input("Enter the Python subject marks :"))
    MySQL=int(input("Enter the MYSQL subject marks :"))
    PowerBI=int(input("Enter the PowerBI subject marks :"))
    Tebular=int(input("Enter the Tebular subject marks :"))
    Excel=int(input("Enter the Excel subject marks :"))
    Average=(Python+MySQL+PowerBI+Tebular+Excel)/5
    print(Average)
    Percentage=(((Python+MySQL+PowerBI+Tebular+Excel)/500)*100)
    print(Percentage,("%"))
    if Percentage>=90:
        print("A Grade")
    elif Percentage>=85:
        print("B Grade")
    elif Percentage>=65:
        print("C Grade")
    elif Percentage>=45:
        print("D Grade")
    elif Percentage>=33:
        print("E Grade")
    else:
        print("__FAIL__")

        
    with open("Students_Record","a")as f:
        f.write(f"Student name :{Name}\n")
        f.write(f"Students roll no :{Roll_no}\n")
        f.write(f"Python Marks:{Python}\n")
        f.write(f"MYSQL Marks : {MySQL}\n")
        f.write(f"PowerBI Marks : {PowerBI}\n")
        f.write(f"Tebular Marks :{Tebular}\n")
        f.write(f"Excel Marks :{Excel}\n")
        f.write(f"Average :{Average}\n")
        f.write(f"Percentage : {Percentage}\n")
        
        if Percentage>=90:
            f.write(("A Grade"))
        elif Percentage>=85:
            f.write("B Grade")
        elif Percentage>=65:
            f.write("C Grade")
        elif Percentage>=45:
            f.write("D Grade")
        elif Percentage>=33:
            f.write("E Grade")
        else:
            f.write("__FAIL__")
add_students()
def View_Students():
       print("\n--- All Student Records ---")
       os.path.exists("Students_Record")
       with open("Students_Record","r")as f:
            for line in f:

             words = line.strip().split(",")
             for item in words:
                print(item)
View_Students()
def Search_student():
    print("\n=======Search_Student=======")
    roll_no=int(input("enter the Student roll no "))
    with open("Students_Record","r") as file:
        data=file.readlines()
        found=False
        for i in range(len(data)):
            if data[i].strip()=="Roll:" +str(roll_no):
                print(data[i-1].strip())
                print(data[i].strip())
                print(data[i+1].strip())
                print(data[i+2].strip())
                print(data[i+3].strip())
                print(data[i+4].strip())
                print(data[i+5].strip())
                print(data[i+6].strip())
                
                found==True
                break
        if found==False:
            print("File not Found")
Search_student()

def analyze_results():
    print("\n======= Analyze_Result =======")

    total_students = 0
    running_total_marks = 0
    passed_students = 0
    failed_students = 0

    with open("Students_Record", "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i].startswith("Student name :"):
            total_students += 1

            # add all 5 subject marks for this student
            student_total = 0
            for j in range(2, 7):   # lines 2 to 6 are marks
                if ":" in lines[i + j]:
                    mark = int(lines[i + j].split(":")[-1].strip())
                    student_total += mark

            running_total_marks += student_total

            percentage = float(lines[i + 8].split(":")[-1].strip())

            if percentage >= 33:
                passed_students += 1
            else:
                failed_students += 1

            i += 10
        else:
            i += 1

    if total_students == 0:
        print("No student records found.")
        return

    average_marks = running_total_marks / total_students

    print(f"Total Students: {total_students}")
    print(f"Running Total of Marks: {running_total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")
analyze_results()
def main():
    while True:
        print("==========================================")
        print("=====Student_Management_System=====")
        print("==========================================")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Result Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_students()
        elif choice == '2':
            View_Students()
        elif choice == '3':
            Search_student()
        elif choice == '4':
            analyze_results()
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()