#!/usr/bin/env python
# coding: utf-8

# In[31]:


import streamlit as st
import requests


# In[32]:


# Base URL for the Flask backend
backend_base_url = "http://127.0.0.1:5000"


# In[33]:


st.set_page_config(page_title="Guten-bot", page_icon="📚",layout="wide")


# In[34]:


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style\style.css")


# In[35]:


# Center-align the user input text
st.markdown("""
    <style>
    input {text-align: center;}
    </style>
""", unsafe_allow_html=True)


# In[36]:


# HEAD SESSION
with st.container():
    st.subheader("Welcom To This Guten-bot :wave:")
    st.title("Classic Book Summarization")
    st.write("[available books >>](https://www.gutenberg.org/)")


# In[37]:


# get summary and get answer
with st.container():
    st.write("---")
    # User input for book name and query
    # book_name = st.text_input("Enter the name of the book:")
    left, right = st.columns((2,1))
    with left:
        st.markdown("#### Enter the name of the book:")
        book_name = st.text_input(" ")
        if book_name:            
            option = st.selectbox("Select an option:", ["Get Summary", "Get Answer"])

            if option == "Get Summary":
                # Button to get book summary
                if st.button("Get Summary"):
                    response = requests.post(f"{backend_base_url}/get_summary", json={"book_name": book_name})
                    book_summary = response.json().get("book_summary")
                    st.write(f"**Book Summary:** {book_summary}")
            elif option == "Get Answer":
                # User input for query
                # query = st.text_input("Enter your query:")
                st.markdown("#### Enter your query:")
                query = st.text_input("  ")

                # Button to get answer
                if st.button("Get Answer"):
                    
                    if not query:
                        st.write("Please enter your query.")
                    else:
                        response = requests.post(f"{backend_base_url}/get_answer", json={"query": query})
                        answer = response.json().get("answer")
                        st.write(f"Answer: {answer}")
        else:
            st.write("Please enter the name of the book to continue.")


# In[40]:


with st.container():
    st.write("---")
    st.header("Get in touch with us :book:")
    st.write("##")

    # from https://formsubmit.co/
    contect_form = """
    <form action="https://formsubmit.co/shabthana.20@cse.mrt.ac.lk" method="POST"> # change the e-mail address if you want
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="feedback" style="text-align: center;" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contect_form, unsafe_allow_html=True)
with right_column:
    st.empty()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




