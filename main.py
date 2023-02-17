print("\nWelcome To My Remaining Life Calculator\n")

age = input("What is your current age?\n")

remaining_age = 90 - int(age)

days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12
hours = days * 24

print(f"You have {hours} hours, {days} days, {weeks} weeks, and {months} months left if you live 90 years.")