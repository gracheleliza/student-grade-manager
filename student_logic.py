def add_student(students, name, grade):
    if len(students) >= 10:
        raise ValueError("Maximum 10 students allowed")

    students.append((name, grade))
    return students


def compute_average(students):
    if not students:
        return 0
    return sum(g for _, g in students) / len(students)


def sort_grades(students):
    return sorted(students, key=lambda x: x[1])


def search_student(students, name):
    for s in students:
        if s[0].lower() == name.lower():
            return s
    return None