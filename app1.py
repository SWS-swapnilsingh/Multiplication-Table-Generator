import streamlit as st

# Setting the title for the Streamlit app
st.title('Multiplication Table Generator')


# Displaying a brief description or instruction
st.write('Welcome! Ready to whip up a multiplication table for any positive number? Let\'s get started!')

# Sidebar section for direct calculation
st.sidebar.header("Quick Multiplication Calculator")
num1 = st.sidebar.number_input("Enter the first number", min_value=0, value=1)
num2 = st.sidebar.number_input("Enter the second number", min_value=0, max_value=100, value=1)
st.sidebar.text(f'Result:  {num1} X {num2} = {num1 * num2}')

# Sidebar section for additional settings
st.sidebar.header("Advanced Settings")
b = 'Feeling ambitious? Generate a multiplication table that goes beyond the usual 10 rows!\n'
upto = st.sidebar.number_input(b, min_value=10, value=10, step=5)



# Main section for generating a multiplication table
number = st.number_input('Enter the number to generate the table for', min_value=0, value=2, step=1)

# Informing the user of the table being generated
st.text(f'Here\'s the multiplication table for {number}, going up to {upto}:')

# List to store the lines of the multiplication table
table_lines = []

# Generating and displaying the multiplication table
for i in range(1, upto + 1):
    table_line = f'{number} X {i} = {number * i}\n'
    table_lines.append(table_line)

# Display each line of the multiplication table
for line in table_lines:
    st.text(line)
