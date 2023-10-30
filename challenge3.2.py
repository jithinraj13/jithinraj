#3.2Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.
def sort_students(student_list):
  # Sort the student_list based on the 'cgpa' attribute in descending order
  sorted_students = sorted(student_list, key=lambda student: student['cgpa'], reverse=True)
  return sorted_students

# Define a list of sample student objects
students = [
  {"name": "Alice", "roll_number": "A123", "cgpa": 3.75},
  {"name": "Bob", "roll_number": "B456", "cgpa": 3.60},
  {"name": "Charlie", "roll_number": "C789", "cgpa": 3.90},
  # Add more students as needed
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['cgpa']}")