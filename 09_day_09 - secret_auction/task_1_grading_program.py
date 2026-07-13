student_scores = {
    'Harry': 88,
    'jeremy': 95,
    'Ibti': 98,
    'Paul': 15,
    'Peter': 0,
    'Mike': 55,
    'Mag': 45,
    'Last': 105, 
}

student_grades = {}

for key in student_scores:
    if 90 < student_scores[key] < 101:
        student_grades [key] = "Outstanding"
    elif 80 < student_scores[key] < 91:
        student_grades [key] = "Exceeds Expectations"
    elif 70 < student_scores[key] < 81:
        student_grades [key] = "Acceptable"
    elif 0 < student_scores[key] < 71:
        student_grades [key] = "Acceptable"
    else:
        student_grades [key] = "Invalid Score"
print(student_grades)
