import streamlit as st
import numpy as np

# Define the calculator function
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operator")

# Define the Streamlit app
st.title("Calculator")

# Get user input
a = st.number_input("First number")
b = st.number_input("Second number")
op = st.selectbox("Operator", ["+", "-", "*", "/"])

# Calculate the result
try:
    result = calculate(a, b, op)
except ZeroDivisionError as e:
    st.error(e)
else:
    st.write("Result:", result)

# Add more operations
st.markdown("Additional operations:")

# Square root
sqrt = np.sqrt(a)
st.write("Square root of {}: {}".format(a, sqrt))

# Logarithm
log = np.log(a)
st.write("Logarithm of {}: {}".format(a, log))

# Exponential
exp = np.exp(a)
st.write("Exponential of {}: {}".format(a, exp))
