while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        break
    
    first_name = input("Enter the student's first name: ")
    
    while True:
        try:
            gpa = float(input("Enter the student's GPA: "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("Error: GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. Please enter a valid GPA as a number.")
    
    if gpa >= 3.5:
        print(f"Congratulations, {first_name} {last_name}! You have made the Dean's List.")
    elif gpa >= 3.25:
        print(f"Great job, {first_name} {last_name}! You have made the Honor Roll.")
    else:
        print(f"Keep working hard, {first_name} {last_name}! Your doing great!")
