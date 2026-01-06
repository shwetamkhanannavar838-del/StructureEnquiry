import pytest
from student import calculate_average, assign_grade   

def test_student_grade():
    # Sample test data
    m1 = 80
    m2 = 90
    m3 = 85

    # Expected result
    # Average = (80 + 90 + 85) / 3 = 85.0 → Grade = A
    expected_average = 85.0
    expected_grade = "A"

    # Function calls
    avg = calculate_average(m1, m2, m3)
    grade = assign_grade(avg)

    # Assertions
    assert avg == expected_average
    assert grade == expected_grade