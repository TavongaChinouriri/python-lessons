my_list = [1, 2, 3]
print(f"Original list: {my_list}")

# Modify an element
my_list[0] = 5
print(f"Modified element: {my_list}")

# Add an element
my_list.append(4)
print(f"Appended element: {my_list}")

# Remove an element
my_list.remove(2)
print(f"Removed element: {my_list}")


my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")

# Attempting to modify an element (will raise a TypeError)
try:
    my_tuple[0] = 5
except TypeError as e:
    print(f"Error: {e}")

# Attempting to add an element (will raise a TypeError)
try:
    my_tuple.append(4)
except AttributeError as e: # Tuples do not have an append method
    print(f"Error: {e}")
    