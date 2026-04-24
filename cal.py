import streamlit as st
st.set_page_config(page_title="Calculater", page_icon="🌍")
st.title("🌍 Calculater")
operation={
    "Sum":"+",
    "subtract":"-",
    "divide":"/",
    "multiply":"*"
}

target_operation = st.selectbox("operation done", list(operation.keys()))
a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

if st.button("operaTE"):
    if target_operation=="sum":
        st.success(a+b)
    elif target_operation=="subtract":
        st.success(a-b)
    elif target_operation=="divide":
        st.success(a/b)
    else :
        st.success(a*b)
