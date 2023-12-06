class Employee:
    """
    Represents an employee in the company.

    Attributes:
    - name (str): Employee's name.
    - age (int): Employee's age.
    - address (str): Employee's address.
    - city (str): Employee's city.
    - state (str): Employee's state.
    - position (str): Employee's position in the company.
    - hire_date (str): Employee's hire date (formatted as "YYYY-MM-DD").
    """

    def __init__(self, name, age, address, city, state, position, hire_date):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.position = position
        self.hire_date = hire_date

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nCity: {self.city}\nState: {self.state}\nPosition: {self.position}\nHire Date: {self.hire_date}"


class EmployeeManager:
    """
    Manages a collection of employees.

    Attributes:
    - employees (list): List of Employee objects.
    """

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the manager."""
        self.employees.append(employee)

    def get_employee(self, name):
        """Get an employee by name."""
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def list_employees(self):
        """List all employees in the manager."""
        for employee in self.employees:
            print(employee)

    def remove_employee(self, name):
        """Remove an employee by name."""
        employee = self.get_employee(name)
        if employee:
            self.employees.remove(employee)
            print(f"{name} has been removed from the employee list.")
        else:
            print(f"Employee with name {name} not found.")

if __name__ == "__main__":
    employee_manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Remove Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            address = input("Enter employee address: ")
            city = input("Enter employee city: ")
            state = input("Enter employee state: ")
            position = input("Enter employee position: ")
            hire_date = input("Enter employee hire date (YYYY-MM-DD): ")

            employee = Employee(name, age, address, city, state, position, hire_date)
            employee_manager.add_employee(employee)
            print(f"{name} has been added to the employee list.")

        elif choice == "2":
            employee_manager.list_employees()

        elif choice == "3":
            name = input("Enter the name of the employee to remove: ")
            employee_manager.remove_employee(name)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select a valid option.")
