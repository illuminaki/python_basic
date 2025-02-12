"""
Program: Grade and Statistics Challenge
This program allows you to:
  1. Determine whether a student passed or failed based on a grade (0-100).
  2. Calculate the average of a list of grades entered by the user.
  3. Count how many grades in the list are above a specific threshold (using a while loop).
  4. Verify and count the occurrence of a specific grade in the list, using a for loop that employs break and continue.
"""

def check_approval():
    """
    Prompts the user to enter a numeric grade (0-100) and determines if the student passed.
    It is assumed that a passing grade is 60 or higher.
    """
    try:
        grade = float(input("Enter a grade (0-100): "))
        # Check if the grade is within the valid range (0 to 100)
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return
    except ValueError:
        # Handle invalid (non-numeric) input
        print("Invalid input. Please enter a numeric value.")
        return

    # Use conditional statements to determine if the grade is passing (>= 60) or failing
    if grade >= 60:
        print("Student approved!")
    else:
        print("Student failed.")

def calculate_average_from_input():
    """
    Prompts the user to enter a list of grades separated by commas,
    converts the input into a list of float numbers, and calculates the average using a for loop.
    Returns the list of grades for use in subsequent functions.
    """
    grades_input = input("Enter a list of grades separated by commas: ")
    try:
        # Convert the input string into a list of numbers (floats)
        grades = [float(x.strip()) for x in grades_input.split(',') if x.strip() != '']
    except ValueError:
        print("One or more grades are invalid.")
        return None

    total = 0
    count = 0
    # Iterate over the list of grades to compute the total and count the number of grades
    for grade in grades:
        total += grade
        count += 1

    if count == 0:
        print("No valid grades entered.")
        return None

    average = total / count
    print(f"The average of the grades is: {average}")
    return grades

def count_grades_above_threshold(grades):
    """
    Asks the user for a threshold value and uses a while loop to count how many grades in the list
    are greater than that threshold.
    """
    try:
        threshold = float(input("Enter a threshold value: "))
    except ValueError:
        print("Invalid threshold value.")
        return

    count = 0
    index = 0
    # Loop through the list using a while loop
    while index < len(grades):
        if grades[index] > threshold:
            count += 1  # Increment count if the current grade is above the threshold
        index += 1

    print(f"There are {count} grades above {threshold}.")

def verify_and_count_specific_grade(grades):
    """
    Prompts the user to enter a specific grade to search for in the list.
    Uses a for loop to iterate over the list:
      - Uses 'continue' to skip elements that do not match the target grade.
      - Uses 'break' to stop the search early if a maximum count (for demonstration purposes) is reached.
    Prints how many times the specific grade appears in the list.
    """
    try:
        target = float(input("Enter the grade to verify: "))
    except ValueError:
        print("Invalid grade input.")
        return

    count_specific = 0
    max_count = 5  # For demonstration: stop counting early if the target grade is found 5 times

    # Iterate over each grade in the list
    for grade in grades:
        # If the current grade does not match the target, skip to the next iteration
        if grade != target:
            continue
        # If the grade matches, increment the count
        count_specific += 1
        # If the maximum count is reached, use break to exit the loop early
        if count_specific == max_count:
            print("Maximum count reached; stopping early.")
            break

    print(f"The grade {target} appears {count_specific} times in the list.")

def main():
    """
    Main function that orchestrates the execution of the program.
    It performs the following tasks sequentially:
      1. Checks if a student passed or failed based on a grade.
      2. Calculates the average of a list of grades.
      3. Counts how many grades are above a specific threshold.
      4. Verifies and counts the occurrence of a specific grade in the list.
    """
    print("=== Approval Check ===")
    check_approval()
    
    print("\n=== Average Calculation ===")
    grades = calculate_average_from_input()
    if grades is None:
        return  # Terminate the program if no valid grades were entered.
    
    print("\n=== Count Grades Above Threshold ===")
    count_grades_above_threshold(grades)
    
    print("\n=== Verify and Count Specific Grade ===")
    verify_and_count_specific_grade(grades)

if __name__ == "__main__":
    main()
