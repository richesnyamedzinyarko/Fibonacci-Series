def generate_fibonacci(n):
    """Generates the Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the sequence with the first two numbers
    series = [0, 1]
    
    # Loop to calculate the rest of the terms
    for i in range(2, n):
        next_value = series[-1] + series[-2]
        series.append(next_value)
        
    return series

def main():
    print("========================================")
    print("      Fibonacci Series Calculator       ")
    print("========================================")
    
    try:
        # Get input from the user
        n_terms = int(input("Enter the number of terms (n): "))
        
        if n_terms <= 0:
            print("Please enter a positive integer greater than 0.")
            return
            
        # Generate the sequence
        result = generate_fibonacci(n_terms)
        
        # Display the output nicely
        print(f"\nThe first {n_terms} terms are:")
        print(result)
        
    except ValueError:
        print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    main()