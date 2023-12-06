user_input = input("Enter class attributes (e.g., attribute1, attribute2): ")
attribute_names = user_input.split(', ')

class_name = 'DynamicClass'
class_attributes = {attr: None for attr in attribute_names}
new_class = type(class_name, (object,), class_attributes)

instance = new_class()
for attr in attribute_names:
    value = input(f"Enter value for attribute '{attr}': ")
    setattr(instance, attr, value)

print("Instance attributes:")
for attr in attribute_names:
    print(f"{attr}: {getattr(instance, attr)}")
