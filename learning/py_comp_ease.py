class ListComprehension:
    """A class for generating Python list comprehensions."""

    def __init__(self):
        """Initialize an instance of ListComprehension."""
        self.variables = []
        self.expressions = []

    def add_variable(self, variable_name):
        """
        Add a variable to the list comprehension.

        :param variable_name: Name of the variable.
        :type variable_name: str
        """
        self.variables.append(variable_name)

    def add_expression(self, expression):
        """
        Add an expression to the list comprehension.

        :param expression: Expression to be included.
        :type expression: str
        """
        self.expressions.append(expression)

    def generate(self):
        """
        Generate a Python list comprehension based on added variables and expressions.

        :return: Generated list comprehension as a string.
        :rtype: str
        """
        if not self.variables or not self.expressions:
            return "Invalid list comprehension, missing variables or expressions."

        comprehension = "["
        comprehension += f"{', '.join(self.variables)} for "
        comprehension += f"{', '.join(self.expressions)} in {', '.join(self.variables)}"
        comprehension += "]"

        return comprehension

if __name__ == "__main__":
    print("Welcome to PyCompEase!")

    lc = ListComprehension()

    while True:
        print("\nOptions:")
        print("1. Add variable")
        print("2. Add expression")
        print("3. Generate list comprehension")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            variable_name = input("Enter variable name: ")
            lc.add_variable(variable_name)
        elif choice == "2":
            expression = input("Enter expression: ")
            lc.add_expression(expression)
        elif choice == "3":
            generated_code = lc.generate()
            print(f"Generated list comprehension: {generated_code}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
