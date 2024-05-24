import streamlit as st
import streamlit.components.v1 as components

st.title("Hello world")

dialogflow_bot = """
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1">
    </script>
    <!--<style>
        df-messenger {
        --df-messenger-bot-message: #878fac;
        --df-messenger-button-titlebar-color: #df9b56;
        --df-messenger-chat-background-color: #fafafa;
        --df-messenger-font-color: white;
        --df-messenger-send-icon: #878fac;
        --df-messenger-user-message: #479b3d;
        }
    </style>-->
    <df-messenger 
    intent="WELCOME"
    chat-title="IPL Buddy"
    agent-id="cc8dfc8c-36c0-420e-9c7b-aeb2ba566a1c"
    language-code="en"
    ></df-messenger>
"""

components.html(dialogflow_bot, height=700)
