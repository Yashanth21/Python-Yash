def is_pass(mark):
    if mark >= 35:
        return True
    return False


def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


def bonus_marks(mark):
    return mark + 5