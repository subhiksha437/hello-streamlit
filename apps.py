def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")
import streamlit as st
st.header("Page Title")

# Add space between the geader and the next item
nl(1)

# Text Prompt
st.markdown("""
            Write Quiz Description and Instructions.
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()
