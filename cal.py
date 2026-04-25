import streamlit as st
st.set_page_config(page_title="Calculater", page_icon="🌍")
st.title("🌍 Calculater")
operation={
    "sum":"+",
    "subtract":"-",
    "divide":"/",
    "multiply":"*"
}

target_operation = st.selectbox("operation done", list(operation.keys())) 
a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

if st.button("operaTE"):
    if target_operation=="sum":
        c=a+b
        st.success(f"result:{c}")
    elif target_operation=="subtract":
        c=a-b
        st.success(f"result:{c}")
    elif target_operation=="divide":
        if b==0:
            st.error("no aplicable")
        else:
            c=a/b
            st.success(f"result:{c}")
    elif target_operation == "multiply":
        c=a*b
        st.success(f"result:{c}")

