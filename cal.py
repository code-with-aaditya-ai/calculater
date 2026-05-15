import streamlit as st
st.set_page_config(page_title="Calculater", page_icon="🌍")
st.title("🌍 Calculater")
if "result" not in st.session_state:
    st.session_state.result = None

operation={
    "sum":"+",
    "subtract":"-",
    "divide":"/",
    "multiply":"*"
}
list={
    "contune calculater":"contune",
    "start new calculater":"new"
}

# SELECT TASK
target_task = st.selectbox(
    "Choose task",
    list(task_list.keys())
)

# SELECT OPERATION
target_operation = st.selectbox(
    "Choose operation",
    list(operation.keys())
)

if target_task == "start new calculator":

    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")

# CONTINUE WITH PREVIOUS RESULT
else:

    st.write(f"Previous Result: {st.session_state.result}")

    a = st.session_state.result
    b = st.number_input("Enter next number")

# CALCULATE
if st.button("Calculate"):

    if a is None:
        st.error("First do a new calculation")

    else:

        symbol = operation[target_operation]

        expression = f"{a}{symbol}{b}"

        try:
            result = eval(expression)

            st.session_state.result = result

            st.success(f"Result: {result}")

        except:
            st.error("Invalid Calculation")
