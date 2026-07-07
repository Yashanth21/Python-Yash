from student import is_pass, calculate_grade, bonus_marks


def test_is_pass():
    assert is_pass(80) == True


def test_is_fail():
    assert is_pass(20) == False


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(80) == "B"


def test_grade_c():
    assert calculate_grade(60) == "C"


def test_grade_fail():
    assert calculate_grade(30) == "Fail"


def test_bonus():
    assert bonus_marks(90) == 95