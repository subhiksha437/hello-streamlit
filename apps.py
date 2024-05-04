import streamlit as st
def main():
    st.title("Events Update")

    st.subheader("Events")
    img=[['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp'],['/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp','/workspaces/hello-streamlit/image/vd img.webp']]
    Date=[['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23'],['2024-04-20', '2024-04-21', '2024-04-22', '2024-04-23']]
    loc=[['chennai', 'tiruchi','tenkasi', 'ooty'],['madurai', 'theni','Location C', 'Location D'],['Location A', 'Location B','Location C', 'Location D'],['Location A', 'Location B','Location C', 'Location D']]
    c=1
    j=0
    for f in range(3):
            col1, col2,col3,col4=st.columns(4)
            with col1:
                st.image(img[f][0], caption=f"Date: {Date[f][0]}, Location: {loc[f][0]}", width=120)
            with col2:
                st.image(img[f][1], caption=f"Date: {Date[f][1]}, Location: {loc[f][1]}", width=120)
            with col3:
                st.image(img[f][2], caption=f"Date: {Date[f][2]}, Location: {loc[f][2]}", width=120)
            with col4:
                st.image(img[f][3], caption=f"Date: {Date[f][3]}, Location: {loc[f][3]}", width=120)  
            



if __name__ == "__main__":
    main()

import streamlit as st
import json


def run():
    st.set_page_config(
        page_title="Streamlit quizz app",
        page_icon="❓",
    )

if __name__ == "__main__":
    run()

# Custom CSS for the buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
</style>
""", unsafe_allow_html=True)

# Initialize session variables if they do not exist
default_values = {'current_index': 0, 'current_question': 0, 'score': 0, 'selected_option': None, 'answer_submitted': False}
for key, value in default_values.items():
    st.session_state.setdefault(key, value)

# Load quiz data
with open('/workspaces/hello-streamlit/k.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False


def submit_answer():

    # Check if an option has been selected
    if st.session_state.selected_option is not None:
        st.session_state.current_index += 1
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False
    else:
        # If no option selected, show a message and do not mark as submitted
        st.warning("Please select an option before submitting.")


# Title and description
st.title("Streamlit Quiz App")

# Progress bar


# Display the question and answer options
question_item = quiz_data[st.session_state.current_index]
st.subheader(f"Question {st.session_state.current_index + 1}")
st.title(f"{question_item['question']}")
st.write(question_item['information'])



# Answer selection
options = question_item['options']
correct_answer = question_item['answer']

if st.session_state.answer_submitted:
    for i, option in enumerate(options):
        label = option
        
else:
    for i, option in enumerate(options):
        if st.button(option, key=i, use_container_width=True):
            st.session_state.selected_option = option
# Submission button and response logic
st.markdown(""" _""")
if st.session_state.selected_option == "NO":
    st.write("You Are In Stage",st.session_state.current_index+1)
    st.button("Go To Task")
        
elif st.session_state.answer_submitted:
    if st.session_state.current_index < len(quiz_data) - 1:
        st.button('Next', on_click=submit_answer)
        
    else:
        st.write(f"Quiz completed!")
        
else:
    if st.session_state.current_index < len(quiz_data):
        st.button('Next', on_click=submit_answer)
