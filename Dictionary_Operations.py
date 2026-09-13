employee = {
    "E1": {"emp_name": "Alex", "designation": "Manager", "dept": "HR", "salary": 80000},
    "E2": {"emp_name": "Gautam", "designation": "Analyst", "dept": "IT", "salary": 60000},
    "E3": {"emp_name": "Sanchita", "designation": "Developer", "dept": "IT", "salary": 75000},
    "E4": {"emp_name": "Mousani", "designation": "Sales Exec", "dept": "Sales", "salary": 55000},
    "E5": {"emp_name": "Daanav", "designation": "Director", "dept": "Finance", "salary": 120000}
}

print(employee["E1"])

print(employee["E4"]["dept"])

max_salary_emp = max(employee.values(), key=lambda x: x["salary"])
print(max_salary_emp)

employee["E6"] = {"emp_name": "Bhagwaan", "designation": "Intern", "dept": "Marketing", "salary": 30000}
print(employee)
