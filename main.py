import time

import pendulum
import streamlit as st
from streamlit.components.v1 import html
from streamlit_chat import message

st.set_page_config(layout="wide")

# Initialize session state variables if they don't exist
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to add a message to the chat
def add_message(author, message):
    st.session_state['messages'].append({'author': author, 'message': message})

# Layout setup
st.title("ChatQ - ")

def on_user_message():
    user_input = st.session_state.user_input # user message
    username = st.session_state.username # username
    st.session_state.messages.append({'username': username, 'user_input': user_input, 'time': pendulum.now()})
    st.session_state.user_input = ""

def on_btn_click():
    del st.session_state.messages[:]



col1, col2 = st.columns([1, 1]) 



with col1:
    st.markdown(
    '''
    <style>
    /* Add your CSS here */
    .chat_container {
        position: fixed;
        bottom: 0;
        width: 100%;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

    chat_container = st.container()
    with chat_container:
        with st.container():
            for i in range(len(st.session_state['messages'])):        
                current_entry = st.session_state['messages'][i]    
                user_input = current_entry['user_input']    
                username = current_entry['username']

                logos = {
                    'Sergey': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Sergey_Brin_Ted_2010.jpg/1264px-Sergey_Brin_Ted_2010.jpg",
                    'Elon': "https://i.guim.co.uk/img/media/f671b8973f4890198f0520a824888a3807f7df71/0_21_2828_1697/master/2828.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=c71f10928e72fce2e97f4f7758a098f1",
                    'Zuck': "https://pbs.twimg.com/media/Dg_ODmOUwAEA3Be.jpg",
                }
                message(user_input, is_user=username == 'Sergey', key=i, logo=logos[username])

        with st.container():
            chat_entry_left, chat_entry_right = st.columns([1, 4]) 
            with chat_entry_right:
                st.text_input("User Input", on_change=on_user_message, key="user_input")

            with chat_entry_left:
                st.selectbox(label='Username', options=['Sergey', 'Elon', 'Zuck'], key='username')
            
st.markdown(
    """
    <style>
    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)




with col2:
    st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
    )
    st.image("https://via.placeholder.com/1024", use_column_width=True)


st.button("Clear history", on_click=on_btn_click)
