"""
Product Validation System

This program calculates the total cost of a purchase in a store.
It prompts the user to enter the following data:
  - Product name (string)
  - Unit price (a positive number)
  - Quantity (a positive integer)
  - Discount percentage (from 0 to 100)
  
The program first calculates the total cost without any discount,
then applies the discount (if any) to compute the final cost.
Finally, it displays the product name along with the final total cost,
formatted with two decimal places.
"""

def get_positive_float(prompt):
    """
    Prompt the user to enter a positive floating-point number.
    Continue prompting until a valid positive number is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("The value must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_positive_int(prompt):
    """
    Prompt the user to enter a positive integer.
    Continue prompting until a valid positive integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("The value must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_discount(prompt):
    """
    Prompt the user to enter a discount percentage between 0 and 100.
    Continue prompting until a valid discount is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("The discount must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_total_cost(price, quantity, discount):
    """
    Calculate the final cost of the purchase.
    
    Steps:
      1. Compute the total cost without discount (price * quantity).
      2. Calculate the discount amount.
      3. Subtract the discount amount from the total cost.
      
    Returns the final cost.
    """
    total_without_discount = price * quantity  # Calculate the cost before discount
    discount_amount = total_without_discount * (discount / 100)  # Calculate discount amount
    total_cost = total_without_discount - discount_amount  # Final cost after discount
    return total_cost

def main():
    """
    Main function that drives the product validation system.
    
    It performs the following steps:
      1. Collect product information from the user.
      2. Validate the input (ensuring numbers are positive and discount is between 0 and 100).
      3. Calculate the final total cost after applying the discount.
      4. Display the product name and the final total cost, formatted with two decimals.
    """
    # Get the product name from the user
    product_name = input("Enter the product name: ").strip()
    
    # Get the unit price; must be a positive number
    unit_price = get_positive_float("Enter the unit price: ")
    
    # Get the quantity; must be a positive integer
    quantity = get_positive_int("Enter the quantity: ")
    
    # Get the discount percentage; must be between 0 and 100
    discount = get_discount("Enter the discount percentage (0-100): ")
    
    # Calculate the final cost after applying the discount
    final_cost = calculate_total_cost(unit_price, quantity, discount)
    
    # Print the results with proper formatting
    print(f"\nProduct: {product_name}")
    print(f"Total Cost after discount: ${final_cost:.2f}")

if __name__ == "__main__":
    main()
