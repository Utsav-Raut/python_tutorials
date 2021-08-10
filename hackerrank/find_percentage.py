# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Input:
# The first line contains the integer 'n', the number of students' records. 
# The next 'n' lines contain the names and marks obtained by a student, each value separated by a space. 
# The final line contains query_name, the name of a student to query.

# Output:
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

print("Enter the number of iterations for which you want to run.")
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
sum, avg = 0, 0
for key, value in student_marks.items():
    # print(key, value)
    if key == query_name:
        for i in value:
            sum = sum + i
avg = sum / 3

print(format(avg, '.2f'))



# Extra Notes:

# name, *line = input().split()
# *line: It's a new unpacking feature introducted in python 3 called star unpacking or extended iterable unpacking.
# check the above link: https://stackoverflow.com/questions/45062375/why-used-before-declaring-a-variable-in-python.

# scores = list(map(float, line))
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
# In the above line, using map, each of the scores are converted to floating point type, and then the scores are appended put in a list