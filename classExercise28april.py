
class Employee:
    def __init__(self, name, experience, hourly_rate, total_hours_worked):
        self.name = name
        self.experience = experience
        self.hourly_rate = hourly_rate
        self.total_hours_worked = total_hours_worked

    def calculate_salary(self):
        base_salary = self.hourly_rate * self.total_hours_worked * 4  # assuming 4 weeks in a month
        if self.experience < 8:
            salary = base_salary
        elif self.experience > 15:
            bonus = base_salary * 0.1
            salary = base_salary + bonus
        else:
            bonus = base_salary * 0.05
            salary = base_salary + bonus

        tax_deduction = salary * 0.13
        final_salary = salary - tax_deduction
        return final_salary



# Example usage
Name = input("Name")
Experience = int(input("Experience"))
hourly_rate = float(input("Hour"))
total_hours_worked = float(input("Hours worked"))

dev = Employee(Name, Experience, hourly_rate, total_hours_worked)
dev_salary = dev.calculate_salary()
print(f"{dev.name}'s salary: ${dev_salary:.2f}")

