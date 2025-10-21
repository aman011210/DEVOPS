# import math
# a=9
# math.factorial(a)
# print(a)
# print("hello")
# print("hell1")
# #this is a comment

# 🧠 1. Basic String Operations

# Concepts: indexing, slicing, concatenation, length, case

# Take input as a string and:

# Take input as a string
user_input = input("Enter something: ")
# Print the first and last character
print(user_input[0], user_input[-1])
# Print the first and last character.

# Print the string in reverse.

# Print every 2nd character.

# Write a program to swap the first and last characters of a string.

# Count the number of vowels and consonants in a given string.

# Check if a string starts and ends with the same character (case-insensitive).

# Convert "devops IS amazing" → "Devops Is Amazing" (proper title case).

# 🔤 2. String Methods Practice

# Concepts: .upper(), .lower(), .split(), .join(), .replace(), .strip()

# Remove all spaces from " Python for DevOps " and print it in uppercase.

# Replace every occurrence of "error" with "issue" in the string "error found in system error log".

# Given "python,aws,docker,jenkins", split it into a list and print each tool on a new line.

# Join a list ["Linux", "Python", "DevOps"] into a single string using " | " as a separator.

# Trim "***Automation***" and print only "Automation" (no *).

# 🔍 3. String Searching & Validation

# Concepts: in, .find(), .count(), .startswith(), .endswith()

# Count how many times "dev" appears in "devdevopsdeveloperdev".

# Check if an email is valid (contains "@" and ends with ".com").

# Find the first and last position of "log" in "logfile_logging_logged".

# Print "Found" if a substring exists in a string, else "Not Found".

# Given a filename "report.log", check if it ends with .log or .txt.

# 🧩 4. String Formatting

# Concepts: f-strings, .format()

# Ask the user for name and tool, and print:
# "Hello Aman, welcome to the Jenkins environment!"

# Given variables service = "Nginx" and status = "Running", print:
# "Service: Nginx | Status: Running"

# Print a message with dynamic spacing using f-strings:
# "Python".center(20, '-')

# 🐍 5. DevOps-Oriented String Questions

# Concepts: practical text parsing, logs, environment variables

# You receive a log line:
# "INFO 2025-10-06 14:30:22 server started successfully"
# Extract and print only the timestamp and message.

# Given an environment variable string:
# "PATH=/usr/bin;USER=ubuntu;SHELL=/bin/bash"
# Convert it into a dictionary like:
# {'PATH': '/usr/bin', 'USER': 'ubuntu', 'SHELL': '/bin/bash'}

# Extract domain name from an email, e.g., "devops@ltimindtree.com" → "ltimindtree.com".

# Check if a given filename has sensitive extensions like .pem, .key, or .env and print a warning.

# Given multiple lines of logs (multi-line string), count how many lines contain "ERROR".

# 💡 6. Mini Project Challenge

# Goal: Combine all string concepts.

# Write a Python program to:

# Take multiple lines of simulated log input.

# Clean extra spaces.

# Convert all text to lowercase.

# Count the number of "error", "warning", and "info" entries.

# Print a summary report like:

# Log Summary:
# INFO: 10
# WARNING: 3
# ERROR: 5

# 🏁 Bonus Challenge

# Write a Python function mask_secret(text) that replaces all characters except the first and last 2 with *.
# Example:
# "awssecretkey" → "a********ey"