# <details>
# <summary>
# 9. List Uniqueness Checker
# </summary>
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# ```python
items = ["apple", "banana", "orange", "apple", "mango"]

unique_value= set()
for item in items:
     if item in unique_value:
         print("duplicate:",item)
         break
     unique_value.add(item)
 
 
# ```
# </details>