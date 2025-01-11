import time
import streamlit as st
import pandas as pd
import numpy as np
import random

st.title("Real-Time Posture Assistant")


#make dynamic user 
username = "John Doe"
st.markdown(f"""
    <h3 style="font-size: 18px; margin-bottom: 10px;">Hi {username}! Here are your stats for <b>Monday, Jan 11, 2025</b></h3>
""", unsafe_allow_html=True)
  
#create 4 boxes
col1, col2 = st.columns([1,1])
col3, col4 = st.columns(2)

with col1:

    st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px; border-radius: 2px; margin: auto;">
            <p style="font-size: 24px; color: green; margin: 0;">72</p>
            <p style="font-size: 14px; color: black; margin: 0;">avg posture score</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px; border-radius: 2px; margin: auto;">
            <p style="font-size: 24px; color: orange; margin: 0;">3</p>
            <p style="font-size: 14px; color: black; margin: 0;">posture corrections</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: black; margin: 0;">5h 35m</p>
            <p style="font-size: 14px; color: black; margin: 0;">avg sitting time</p>
        </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: red; margin: 0;">1h 02m</p>
            <p style="font-size: 14px; color: black; margin: 0;">spent in bad posture</p>
        </div>
    """, unsafe_allow_html=True)


# Current posture value from 0 to 1, 0 being the worst and 1 being the best 
current_posture = 0.6

line_chart_data = pd.DataFrame(
    np.random.randn(0, 1),
    columns=['posture']
)

# centered title for the chart
st.markdown(f"""
    <h3 style="font-size: 22px; margin-top: 10px; margin-bottom: 10px; text-align: center; ">Your posture score over time</h3>
            """, unsafe_allow_html=True) 
chart = st.line_chart(line_chart_data)
    
#Analysis section begins here - Note: 
st.markdown(
    "<span style='font-size: 30px; display: block;'><strong>Analysis</strong></span>",
    unsafe_allow_html=True
)
today_score = random.randint(60, 80)
yesterday_score = random.randint(50, 70)
time_in_bad_posture = random.randint(30, 90)  # in minutes
streak_days = random.randint(3, 7)

st.markdown(f"<p style='font-size: 18px;'>Your posture score today is <strong>{today_score}</strong>.</p>", unsafe_allow_html=True)

if today_score > yesterday_score:
    st.markdown("<p style='font-size: 18px;'>Great job! You've improved your posture compared to yesterday.</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='font-size: 18px;'>Keep working on improving your posture. Remember to sit upright and take frequent breaks.</p>", unsafe_allow_html=True)

if time_in_bad_posture > 60:
    st.markdown("<p style='font-size: 18px; color: orange;'>You spent over an hour in bad posture today. Try to take regular breaks and adjust your sitting position.</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='font-size: 18px; color: green;'>Good job! You spent less than an hour in bad posture today.</p>", unsafe_allow_html=True)

st.markdown(f""" <span style ='font-size:30px;'><strong>Recommendations</strong></span> """, unsafe_allow_html=True)


while True: 
    time.sleep(0.5) 
    chart.add_rows(pd.DataFrame([current_posture], columns=['posture']))



# Fill the columns with styled data






