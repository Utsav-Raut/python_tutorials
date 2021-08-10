# Program statement
# Input a list which contains smaller lists of two values - student name and score
# Find out the student with second lowest score and display
# If there are multiple students with second lower score, then display their names in dictionary order

# Input:
# Number of students details you want to check and for each such student enter their name and score

# Output:
# Student name(s) with the second lowest score

student_details = []
stud_score = set()
second_lowest_stud_details = []
print("Enter the details:")

for _ in range(int(input())):
    name = input()
    score = float(input())
    student_details.append([name, score])
    stud_score.add(score)

print(student_details)

second_lowest_score = sorted(stud_score)[1]
print(sorted(stud_score))
print("Second highest score = ",second_lowest_score)

for name, score in student_details:
    if score == second_lowest_score:
        second_lowest_stud_details.append(name)

for name in (sorted(second_lowest_stud_details)):
    print(name, end="\n")

