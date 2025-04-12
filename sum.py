import re

# Files to process
filenames = ['regex_sum_42.txt', 'regex_sum_2193011.txt']

total = 0  # Avoid using "sum" (conflict with built-in function)

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            # Read entire file content and extract numbers
            numbers = re.findall(r'[0-9]+', file.read())
            total += sum(int(num) for num in numbers)
        print(f"Processed: {filename}")
    except FileNotFoundError:
        print(f"Error: {filename} not found. Skipping...")

print("\nTotal sum of all numbers:", total)