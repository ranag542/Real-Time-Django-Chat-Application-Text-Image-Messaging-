from math_operations import MathOperations

# Main driver code
if __name__ == "__main__":
    # Example tuple
    numbers = (5, 2)

    # Create an instance of MathOperations
    operations = MathOperations(numbers)

    choice = input("Enter A for Addition, S for Subtraction, M for Multiplication, D for Division, P for Power: ").upper()

    if choice == 'A':
        print("Result:", operations.Addition())
    elif choice == 'S':
        print("Result:", operations.Subtraction())
    elif choice == 'M':
        print("Result:", operations.Multiplication())
    elif choice == 'D':
        print("Result:", operations.Division())
    elif choice == 'P':
        print("Result:", operations.Power())
    else:
        print("Invalid choice!")
