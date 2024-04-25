def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")
import streamlit as st
st.header("STAGE PREDICTION ASESSMENT")

nl(1)

# Text Prompt
st.markdown("""
            1. This quiz contains 15 questions and all the questions must be answered.
            2. Based on the answers given, your current stage will be decided.
            3. Analyse each question and answer. ALL THE BEST!!!
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()


st.button("Reset", type="primary")
if st.button('Start the test'):
    st.write('Wait for a min....')
else:
    st.write('Click the button')