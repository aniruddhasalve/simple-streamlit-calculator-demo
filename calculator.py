import streamlit as st

st.title("Simple Calculator")

def calculate(num1, num2, operation):
    """Performs a mathematical operation on two numbers."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Choose operation:", ["+", "-", "*", "/"])

result = calculate(num1, num2, operation)
st.success(f"The result is: {result}")
