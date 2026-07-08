from employee import (
    get_employee_name,
    calculate_salary,
    calculate_bonus,
    is_eligible_for_promotion
)

employee_name = get_employee_name("Yash")
salary = calculate_salary(30, 1000)
bonus = calculate_bonus(salary)
promotion = is_eligible_for_promotion(6)

print(employee_name)
print(f"Salary: {salary}")
print(f"Bonus: {bonus}")
print(f"Eligible for Promotion: {promotion}")