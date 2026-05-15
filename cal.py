import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Smart Calculator")

# Save previous result
if "result" not in st.session_state:
    st.session_state.result = None

task = st.selectbox(
    "Choose option",
    [
        "New Calculation",
        "Continue With Previous Result"
    ]
)

# NEW CALCULATION
if task == "New Calculation":

    expression = st.text_input(
        "Enter expression"
    )

# CONTINUE WITH PREVIOUS RESULT
else:

    st.write(f"Previous Result: {st.session_state.result}")

    next_expression = st.text_input(
        "Enter operation with next value",
        placeholder="Example: +10 or *2"
    )

    if st.session_state.result is not None:
        expression = str(st.session_state.result) + next_expression
    else:
        expression = ""

# CALCULATE BUTTON
if st.button("Calculate"):

    if expression.strip() == "":
        st.warning("Please enter expression")

    else:
        try:
            result = eval(expression)

            st.session_state.result = result

            st.success(f"Result: {result}")

        except:
            st.error("Invalid Expression")
