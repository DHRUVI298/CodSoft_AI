# Task 1
# DABHI DHRUVI R
import streamlit as st
from groq import Groq
import config
from langchain.chains import conversation
from langchain_groq import ChatGroq
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import  http    
import os

groq_api_key = "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"
def main():
        st.subheader(":blue[ChatBoat App]")
        st.write("----")
        conversation_memory_length = st.sidebar.slider(':blue[Conversational Meomory Length:]',1,10,value=5)
        memory = ConversationBufferMemory(k=conversation_memory_length)
        user_question  = st.text_area(":black[Ask A Question...]")    
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history=[]
            #1
            st.session_state.selected_question = None
        else:
            for message in st.session_state.chat_history:
                memory.save_context({'input':message['human']},{'output':message['AI']})                    
            groq_chat = ChatGroq(        
            groq_api_key  = groq_api_key,
            model_name = "mixtral-8x7b-32768")
            
            conversation = ConversationChain(
                llm = groq_chat,
                memory = memory
                
            )
            if user_question:
                if st.session_state.selected_question is None:

                    response = conversation(user_question)
                    message = {'human':user_question,'AI':response['response']}

                    st.session_state.chat_history.append(message)

                    st.write("Chatbot : ",response['response'])
            
                else:
                    st.write(":green[select from chat history]")
            
if __name__  == '__main__':
    main()