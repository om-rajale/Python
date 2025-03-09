# Function to calculate average and determine grade
def calculate_grade(marks):      
    average = sum(marks) / len(marks)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"            
    elif average >= 60: 
        grade = "D"
    else:    
        grade = "F"       
    
    return average, grade
              
# Get student name and marks
student_name = input("Enter student's name: ")
num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Calculate average and grade
average, grade = calculate_grade(marks)

# Display the result
print(f"\nStudent Name: {student_name}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
