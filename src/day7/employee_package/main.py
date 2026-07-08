from employee import *

salary = calculate_salary(30, 1000)

print(get_employee_name("Yash"))
print("Salary:", salary)
print("Bonus:", calculate_bonus(salary))
print("Promotion:", is_eligible_for_promotion(6))