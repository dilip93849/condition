age = int(input("Enter age: "))
experience = input("Do you have experience? (yes/no): ")

if age > 18:
    if experience.lower() == "yes":
        print("Eligible for job")
    else:
        print("Not eligible (no experience)")
else:
    print("Not eligible (underage)")
