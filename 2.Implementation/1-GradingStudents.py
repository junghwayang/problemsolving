def gradingStudents(grades):
    return [i+5 - (i%5) if i >= 38 and i % 5 >= 3 else i for i in grades]