import tkinter as tk

class ListComprehensionGUI:
    """
    A GUI application for PyCompEase that allows users to add variables and expressions interactively and generate list comprehensions.
    """

    def __init__(self, root):
        """
        Initialize the ListComprehensionGUI.

        :param root: The root Tkinter window.
        :type root: tk.Tk
        """
        self.root = root
        self.root.title("PyCompEase")

        self.variables = []
        self.expressions = []

        # Create labels and entry widgets
        self.variable_label = tk.Label(root, text="Variable Name:")
        self.variable_label.pack()
        self.variable_entry = tk.Entry(root)
        self.variable_entry.pack()

        self.expression_label = tk.Label(root, text="Expression:")
        self.expression_label.pack()
        self.expression_entry = tk.Entry(root)
        self.expression_entry.pack()

        # Create buttons
        self.add_variable_button = tk.Button(root, text="Add Variable", command=self.add_variable)
        self.add_variable_button.pack()
        self.add_expression_button = tk.Button(root, text="Add Expression", command=self.add_expression)
        self.add_expression_button.pack()
        self.generate_button = tk.Button(root, text="Generate List Comprehension", command=self.generate)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_variable(self):
        """
        Add a variable to the list of variables based on user input from the GUI entry field.
        """
        variable_name = self.variable_entry.get()
        self.variables.append(variable_name)
        self.variable_entry.delete(0, tk.END)

    def add_expression(self):
        """
        Add an expression to the list of expressions based on user input from the GUI entry field.
        """
        expression = self.expression_entry.get()
        self.expressions.append(expression)
        self.expression_entry.delete(0, tk.END)

    def generate(self):
        """
        Generate a Python list comprehension based on added variables and expressions and display the result in the GUI.
        """
        if not self.variables or not self.expressions:
            self.result_label.config(text="Invalid list comprehension, missing variables or expressions.")
        else:
            comprehension = "[" + f"{', '.join(self.variables)} for {', '.join(self.expressions)} in {', '.join(self.variables)}" + "]"
            self.result_label.config(text=f"Generated list comprehension: {comprehension}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListComprehensionGUI(root)
    root.mainloop()
