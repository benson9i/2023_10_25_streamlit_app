# cd /Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/
# streamlit run 💹-Charts.py

# ---- Load dependencies ----
import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
from streamlit_lottie import st_lottie

# Load the data
data = pd.read_csv("data/consulting_data.csv")

# ---- Lottie Animation Below Chat ----
def load_lottiefil(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_mentalhealth = load_lottiefil("lottie/mentalhealth_lottie.json")    

# ---- Page setup ----
st.set_page_config(layout="wide")
st.title(":brain: Burnout Syndrom in Consulting")

# ---- Sidebar set up ----
st.sidebar.header("Set Filters")

# Age Filter
min_age, max_age = int(data["age"].min()), int(data["age"].max())
age_range = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))

# Gender Filter
gender_options = data["gender"].unique().tolist()
selected_gender = st.sidebar.multiselect("Select Gender", gender_options, default=gender_options)

# Workload Filter
workload_options = data["workload"].dropna().unique().tolist()
selected_workload = st.sidebar.multiselect("Select Workload", workload_options, default=workload_options)

# Sleep Filter
sleep_options = data["sleep"].unique().tolist()
selected_sleep = st.sidebar.multiselect("Select Sleep Quality", sleep_options, default=sleep_options)

# Experience Filter
experience_options = data["experience"].unique().tolist()
selected_experience = st.sidebar.multiselect("Select Experience Level", experience_options, default=experience_options)

# Reset button
if st.sidebar.button("Reset to Default"):
    age_range = (min_age, max_age)
    selected_gender = gender_options
    selected_workload = workload_options
    selected_sleep = sleep_options
    selected_experience = experience_options

# Filtering the data based on user's input
filtered_data = data[(data["age"] >= age_range[0]) & (data["age"] <= age_range[1])]

if selected_gender:
    filtered_data = filtered_data[filtered_data["gender"].isin(selected_gender)]
if selected_workload:
    filtered_data = filtered_data[filtered_data["workload"].isin(selected_workload)]
if selected_sleep:
    filtered_data = filtered_data[filtered_data["sleep"].isin(selected_sleep)]
if selected_experience:
    filtered_data = filtered_data[filtered_data["experience"].isin(selected_experience)]

# Define the columns
col1_1, col2_1, col3_1 = st.columns([1,2,4], gap="small")

# Subheader and description inside left column (col1_1)
with col1_1:
    st_lottie(lottie_mentalhealth,
              height=125,
              width=125)
# Calculate the total number of participants and display in right column (col2_1)
total_participants = len(filtered_data)    
with col2_1:
    # Use st.markdown with raw HTML to display the total participants in a larger font
    st.markdown(f"""
                <div style="display: flex; flex-direction: column; justify-content: center; height: 100%; padding: 5px 5px;">
                    <div style="font-size: 24px; font-weight: bold; font-family: 'Arial'; ">Total Participants</div>
                    <div style="font-size: 48px;color: #4BDCFF;">{total_participants}</div>
                """, unsafe_allow_html=True)    

with col3_1:
    st.subheader("Introduction")
    st.write("On this page you can see the results of a study investigating the prevalence of burnout in the consulting sector. If you want to talk about this matter, feel free to reach out to me.")

st.write("---")

# ---- Charts set up ----
st.subheader("Demographics")
# Row 1: Gender and Age
# Column 1, Row 1: Donut Chart of Gender
col1_1, col2_1 = st.columns(2, gap="small")
gender_counts = filtered_data['gender'].value_counts()
fig_gender = px.pie(gender_counts, names=gender_counts.index, values=gender_counts.values, title="Gender Distribution", hole=0.3, width=400, height=350, color_discrete_sequence=['#4BDCFF'])
fig_gender.update_layout(showlegend=False)
col1_1.plotly_chart(fig_gender)

# Column 2, Row 1: Histogram for Age
age_hist = px.histogram(filtered_data, x='age', nbins=50, color_discrete_sequence=['#4BDCFF'], title="Age Distribution", height=350, width=700,)
age_hist.update_layout(xaxis_title_text='', yaxis_title_text='')
col2_1.plotly_chart(age_hist)

# Row 2: Experience, Workload, Sleep

# Column 1, Row 2: Barchart of Experience
col1_2, col2_2, col3_2 = st.columns(3, gap="small")
experience_counts = filtered_data['experience'].value_counts()
fig_experience = px.bar(experience_counts, x=experience_counts.index, y=experience_counts.values, title="Distribution of Experience Levels", width=400, height=350, color_discrete_sequence=['#4BDCFF'])
fig_experience.update_layout(xaxis_title_text='', yaxis_title_text='')
col1_2.plotly_chart(fig_experience)

# Column 2, Row 2: Barchart of Workload
workload_counts = filtered_data['workload'].value_counts()
fig_workload = px.bar(workload_counts, x=workload_counts.index, y=workload_counts.values, title="Distribution of Workload", width=400, height=350, color_discrete_sequence=['#4BDCFF'])
fig_workload.update_layout(xaxis_title_text='', yaxis_title_text='')
col2_2.plotly_chart(fig_workload)

# Column 3, Row 2: Barchart of Sleep
sleep_counts = filtered_data['sleep'].value_counts()
fig_sleep = px.bar(sleep_counts, x=sleep_counts.index, y=sleep_counts.values, title="Distribution of Sleep Quality", width=400, height=350, color_discrete_sequence=['#4BDCFF'])
fig_sleep.update_layout(xaxis_title_text='', yaxis_title_text='')
col3_2.plotly_chart(fig_sleep)

st.write("---")

