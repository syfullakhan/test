# Importing the necessary library
import streamlit as st

# Setting the title of the application
st.title("Even or Odd Number Checker")

# Providing a description of the application
st.write("This application takes a number as input and determines if it is even or odd.")

# Creating a number input field
number = st.number_input("Enter a number:", value=0)  # Default value is set to 0

# Function to check if the number is even or odd
def check_even_odd(num):
    if num % 2 == 0:  # Checking if the number is divisible by 2
        return "even"  # If it is, return 'even'
    else:
        return "odd"  # If not, return 'odd'

# Displaying the result when the button is clicked
if st.button("Check"):
    # Handling edge cases
    if number < 0:
        st.error("Please enter a non-negative number.")  # Error message for negative numbers
    else:
        result = check_even_odd(number)  # Call the function to check the number
        st.success(f"The number {number} is {result}.")  # Display the result

# Providing additional information
st.write("### Edge Cases Handled:")
st.write("- **0** is considered even.")
st.write("- **Negative numbers** are not allowed.")
