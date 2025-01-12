import time
import streamlit as st
import pandas as pd
import numpy as np
import random

#Note: currently using randint for now
total_time = 1
today_score = 0
yesterday_score = 0
time_in_bad_posture = 0
time_in_good_posture = 0 
streak_days = 0
running_sum = 0 
samples = 0 

st.image("spine_guard_logo_1.jpg")
st.title("Real-Time Posture Assistant")

#make dynamic user 
username = "John Doe"
st.markdown(f"""
    <h3 style="font-size: 18px; margin-bottom: 10px;">Hi {username}! Here are your stats for <b>Monday, Jan 11, 2025</b></h3>
""", unsafe_allow_html=True)

button = st.button("Zero Posture")
  
#create 4 boxes
col1, col2 = st.columns([1,1])
col3, col4 = st.columns(2)
average_score_text = None 
bad_time_text = None
good_time_text = None

with col1:

    average_score_text = st.markdown("""
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
    
    good_time_text = st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: black; margin: 0;">5h 35m</p>
            <p style="font-size: 14px; color: black; margin: 0;">Time in good posture</p>
        </div>
    """, unsafe_allow_html=True)


with col4:
    bad_time_text = st.markdown("""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: red; margin: 0;">1h 02m</p>
            <p style="font-size: 14px; color: black; margin: 0;">spent in bad posture</p>
        </div>
    """, unsafe_allow_html=True)


# Current posture value from 0 to 1, 0 being the worst and 1 being the best 
current_posture = 100

line_chart_data = pd.DataFrame(
    np.random.randn(0, 1),
    columns=['posture']
)

chart = st.line_chart(line_chart_data, use_container_width=True)

# centered title for the chart
st.markdown(f"""
    <h3 style="font-size: 22px; margin-top: 10px; margin-bottom: 10px; text-align: center; ">Your posture score over time</h3>
            """, unsafe_allow_html=True) 



#Analysis section begins here 
st.markdown(
    "<span style='font-size: 30px; display: block;'><strong>Analysis</strong></span>",
    unsafe_allow_html=True
)



posture_score = st.markdown(f"<p style='font-size: 18px;'>Your posture score today is <strong>{today_score}</strong>.</p>", unsafe_allow_html=True)


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
goal = st.slider("Drag the bar to set your goal", min_value=0, max_value=100, value=75)
st.write(f"Your goal for tomorrow is to achieve a posture score of **{goal}**.")


st.markdown(f""" <span style ='font-size:30px;'><strong>Recommendations</strong></span> """, unsafe_allow_html=True)
st.markdown("View the exerice demonstration and read it's description")
col1, col2, col3, col4 = st.columns(4)


with col1:
    # st.image("400x400_Exercises_to_Relieve_Upper_Back_Pain_Neck_Side_Bend_and_Rotation (1).gif", caption = "neck roll")
#     st.markdown("""
#     <figure style="text-align: center;">
#         <img src="https://post.healthline.com/wp-content/uploads/2019/03/400x400_Exercises_to_Relieve_Upper_Back_Pain_Neck_Side_Bend_and_Rotation.gif" alt="Neck Roll" style="width: 100%; max-width: 800px; border-radius: 8px; border-radius: 2px;">
#         <figcaption style="font-size: 20px; color: gray;">Neck Roll</figcaption>
#     </figure>
# """, unsafe_allow_html=True) 
    st.markdown("![Alt Text](https://post.healthline.com/wp-content/uploads/2019/03/400x400_Exercises_to_Relieve_Upper_Back_Pain_Neck_Side_Bend_and_Rotation.gif)")
    #st.markdown("<p style='font-size: 18px; color: black;'>Neck Roll</p>", unsafe_allow_html=True)
    if st.button("Neck Roll"):
        st.markdown("""
            <p style='font-size: 16px; color: black;'>
            <b>Neck Roll:</b> This exercise helps improve neck flexibility and relieve tension. 
            Slowly tilt your head from side to side in a circular motion.
            </p>
        """, unsafe_allow_html=True)
   
with col2:
    st.markdown("![Alt Text](https://evolvewellnessvancouver.ca/wp-content/uploads/2024/04/1-14cQB3ClUvpYLn-OYHvw3A.gif)") 
    #st.markdown("<p style='font-size: 18px; color: black;'>Chair Rotations</p>", unsafe_allow_html=True)
    if st.button("Chair Rotations"):
        st.markdown("""
            <p style='font-size: 16px; color: black;'>
            <b>Chair Rotations:</b> This stretch loosens up your back muscles and improves posture.
            Sit upright and twist your torso to the side, holding the back of your chair.
            </p>
        """, unsafe_allow_html=True)
  
    # st.markdown("![Alt Text](https://evolvewellnessvancouver.ca/wp-content/uploads/2024/04/1-14cQB3ClUvpYLn-OYHvw3A.gif)")
with col3:
    st.markdown("![Alt Text](https://i0.wp.com/cdn-prod.medicalnewstoday.com/content/images/articles/325/325373/shoulder-roll-stretch-and-exercise-gif.gif?w=315&h=840)") 
    #st.markdown("<p style='font-size: 18px; color: black;'>Shoulder Roll</p>", unsafe_allow_html=True)
    if st.button("Shoulder Roll"):
        st.markdown("""
            <p style='font-size: 16px; color: black;'>
            <b>Shoulder Roll:</b> This stretch relieves tension in the shoulders and upper back. 
            Roll your shoulders forward and backward in a circular motion.
            </p>
        """, unsafe_allow_html=True)

with col4:
    st.markdown("![Alt Text](https://i0.wp.com/post.healthline.com/wp-content/uploads/2019/03/400x400_Exercises_to_Relieve_Upper_Back_Pain_Overhead_Arm_Reach.gif?h=840)")
    #st.markdown("<p style='font-size: 18px; color: black;'>Overhead Arm Reach</p>", unsafe_allow_html=True)
    if st.button("Overhead Arm Reach"):
        st.markdown("""
            <p style='font-size: 16px; color: black;'>
            <b>Overhead Arm Reach:</b> his stretch improves shoulder mobility and relieves upper back tension. 
            Raise your arms overhead, stretch upward, and hold for 10-20 seconds to elongate your spine and improve posture.
            </p>
        """, unsafe_allow_html=True)

offset = 0



# Display iamge
image = st.image("good_posture.png", caption="Good Posture")

while True: 
    # Update the line chart with the new post erdata 
    time.sleep(0.2) 
    # Read the current posture from the posture.txt file
    with open('posture.txt', 'r') as f:
        current_posture = float(f.read())
    chart.add_rows(pd.DataFrame([current_posture - offset], columns=['posture']))

    if button:
        offset = current_posture

    # update variables for posture
    if (current_posture-offset < 40):
        time_in_good_posture += 1/60 
    if (current_posture-offset > 40):
        time_in_bad_posture += 1/60 

    today_score = 100 * time_in_good_posture / total_time 

    running_sum += today_score
    samples += 1

    # Update the average score text
    average_score_text.markdown(f"""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px; border-radius: 2px; margin: auto;">
            <p style="font-size: 24px; color: green; margin: 0;">{running_sum/samples:.2f}</p>
            <p style="font-size: 14px; color: black; margin: 0;">avg posture score</p>
        </div>
    """, unsafe_allow_html=True)
    bad_time_text.markdown(f"""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: red; margin: 0;">{time_in_bad_posture:.0f}m</p>
            <p style="font-size: 14px; color: black; margin: 0;">spent in bad posture</p>
        </div>
    """, unsafe_allow_html=True)

    good_time_text.markdown(f"""
        <div style="text-align: center; background-color: #f3f3f3; padding: 10px;border-radius: 2px; margin:auto;">
            <p style="font-size: 24px; color: black; margin: 0;">{time_in_good_posture:.0f}m</p>
            <p style="font-size: 14px; color: black; margin: 0;">Time in good posture</p>
        </div>
    """, unsafe_allow_html=True)


    # Check if the posture is bad then put the bad iamge
    if current_posture-offset < 10:
        image.image("good_posture.png", caption="Good Posture")
    elif current_posture-offset < 15: 
        image.image("mid_posture.jpg" , caption="Mid Posture")
    elif current_posture-offset < 25: 
        image.image("worst_posture.png", caption="Bad Posture")
    elif current_posture-offset >= 25: 
        image.image("bad_posture.png", caption="Worst Posture")


    posture_score.write(f"<p style='font-size: 18px;'>Your posture score today is <strong>{today_score}</strong>.</p>", unsafe_allow_html=True)

    # update the score  
    total_time += 1/60 

