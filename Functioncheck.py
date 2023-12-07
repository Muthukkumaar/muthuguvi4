# Function to check if an element is an integer or string
check_type = lambda x: (type(x) is int) or (type(x) is str)

# Sample list
my_list = [1, 'hello', 3, 'world', 5]

# Use map with the lambda function to check types of elements
result = list(map(check_type, my_list))

# Print the result
print(result)
