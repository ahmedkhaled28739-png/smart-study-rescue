import streamlit as st

# Application Title
st.title("Interactive Python Calculator")

# User Input for Numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2   = st.number_input("Enter the second number", value=0.0)

# Calculate Button
if st.button("Calculate Result"):
    st.write("---")
    st.write(f"*Addition (+):* {name1 + name2}")
    st.write(f"*Subtraction (-):* {name1 - name2}")
    st.write(f"*Multiplication ():** {name1 * name2}")
    
    if name2 != 0:
        st.write(f"*Division (/):* {name1 / name2}")
        st.write(f"*Modulus (%):* {name1 % name2}")
    else:
        st.error("Cannot divide by zero!")
        