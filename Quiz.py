import streamlit as st

st.write("Hello Students!")
score = 0
st.write("Welcome to quiz game....")

# Q1
st.write("Q1. What is the first alphabet of English language?")
ans1 = st.text_input("Enter answer for Q1 (A/B/C/D)", key="q1")

# Q2
st.write("Q2. What is the National Bird?")
ans2 = st.text_input("Enter answer for Q2 (A/B/C/D)", key="q2")

# Q3
st.write("Q3. What is the National Animal?")
ans3 = st.text_input("Enter answer for Q3 (A/B/C/D)", key="q3")

# Q4
st.write("Q4. What is middle alphabet in CAT?")
ans4 = st.text_input("Enter answer for Q4 (A/B/C/D)", key="q4")

# Q5
st.write("Q5. What is the national vegetable?")
ans5 = st.text_input("Enter answer for Q5 (A/B/C/D)", key="q5")

# Submit button
if st.button("Submit Quiz"):

    score = 0

    if ans1.lower() == "a":
        score += 5
    if ans2.lower() == "a":
        score += 5
    if ans3.lower() == "a":
        score += 5
    if ans4.lower() == "d":
        score += 5
    if ans5.lower() == "d":
        score += 5

    if score == 25:
        st.write("Congratulations! You scored", score, "1st Position")
        st.balloons()
    elif score >= 15:
        st.write("Congratulations! You scored", score, "2nd Position")
        st.snow()
    else:
        st.write("You scored", score, "Better luck next time")
