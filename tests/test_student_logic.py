from student_logic import add_student, compute_average, sort_grades, search_student


def test_add_student():
    students = []
    students = add_student(students, "Alice", 90)
    assert students == [("Alice", 90)]


def test_compute_average():
    students = [("Alice", 90), ("Bob", 80)]
    avg = compute_average(students)
    assert avg == 85


def test_sort_grades():
    students = [("Alice", 90), ("Bob", 80)]
    sorted_students = sort_grades(students)
    assert sorted_students == [("Bob", 80), ("Alice", 90)]


def test_search_student_found():
    students = [("Alice", 90), ("Bob", 80)]
    result = search_student(students, "Alice")
    assert result == ("Alice", 90)


def test_search_student_not_found():
    students = [("Alice", 90)]
    result = search_student(students, "John")
    assert result is None