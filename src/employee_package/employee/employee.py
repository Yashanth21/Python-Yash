def get_employee_name(name):
    return f"Employee Name: {name}"


def calculate_salary(days, salary_per_day):
    return days * salary_per_day


def calculate_bonus(salary):
    return salary * 0.10


def is_eligible_for_promotion(experience):
    return experience >= 5