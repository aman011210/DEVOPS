# <details>
# <summary>1. Age Group Categorization
# </summary>
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# </details>
age =input("enter your age")
if age <13:
    print("child")
elif age <=13 and age <=19:
    print("Teenager")
elif age<=20 and age <=59:
     print("Adult")
elif age >60:
     print("Mature")
