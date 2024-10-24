import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Text input from the user
user_input = st.text_input("Hello google:")

# Button to process the input
if st.button("Submit"):
    if user_input:
        # Display the input text in a formatted way
        st.write("You entered:", user_input)
        # Add some processing logic if needed
        st.write("Processed text:", user_input.upper())  # Example processing
    else:
        st.warning("Please enter some text before submitting.")

# Sidebar for additional options
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2"])

if option == "Option 1":
    st.sidebar.write("You selected Option 1.")
else:
    st.sidebar.write("You selected Option 2.")
