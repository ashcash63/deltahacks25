import time
import streamlit as st
import pandas as pd
import numpy as np
import random

st.image("spine_guard_logo_1.jpg")
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
    
#Analysis section begins here 
st.markdown(
    "<span style='font-size: 30px; display: block;'><strong>Analysis</strong></span>",
    unsafe_allow_html=True
)

#Note: currently using randint for now
total_time = 1
today_score = random.randint(60, 80)
yesterday_score = random.randint(50, 70)
time_in_bad_posture = random.randint(30, 90)  # in minutes
time_in_good_posture = 60 - time_in_bad_posture 
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



# set goals for tomorrow
st.markdown("Set a goal for tomorrow!")
goal = st.slider("Set your goal for tomorrow's posture score", min_value=0, max_value=100, value=75)
st.write(f"Your goal for tomorrow is to achieve a posture score of **{goal}**.")

st.markdown(f""" <span style ='font-size:30px;'><strong>Recommendations</strong></span> """, unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    # st.image("400x400_Exercises_to_Relieve_Upper_Back_Pain_Neck_Side_Bend_and_Rotation (1).gif", caption = "neck roll")
    st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
with col2:
    # st.image("Shoulder-roll.gif", caption = "shoulder roll")
with col3:
    # s
    ...

while True: 

    # CODE TO READ POSTURE FROM SENSOR GOES BELOW 
    
    # Update the line chart with the new post erdata 
    time.sleep(0.5) 
    chart.add_rows(pd.DataFrame([current_posture], columns=['posture']))
    
    # update variables for posture
    if (current_posture < 40):
        time_in_bad_posture += 1/60 
    if (current_posture > 60):
        time_in_good_posture += 1/60
    today_score = time_in_good_posture / total_time  
    
    total_time += 1/60 




# Fill the columns with styled data






