# cd /Users/bennson/Desktop/DataScienceJourney/Streamlit/streamlit_published_app/
# streamlit run 💹-Charts.py

import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_lottie import st_lottie
import json


# ---- Path settings -----
resume_file = "assets/CV.pdf"
profile_pic = "assets/headshot.png"

# ---- General settings ----
page_title = "Digital CV | Dominik Bernard"
page_icon = ":books:"
name_db = "Dominik Bernard"
description = """
I am a psychologist and hold a bachelor's degree in Business Psychology and two master's in Business Psychology and International Management.
Moreover, I am working as a client-facing consulting data scientist (strategy consultant) for Roland Berger. 
"""
email = "dominik.bernard98@googlemail.com"
phone = "004915228913027"

st.set_page_config(page_title=page_title,
                   page_icon=page_icon, layout="centered")
st.title(":memo: Welcome! Check out my CV")


# ---- Load PDF and PNG -----
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ---- Hero section ----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(name_db)
    st.write(description)
    st.download_button(
        label="📂 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
    )
    st.write("📧", email)
    st.write("📲", phone)

# ---- Skills ----
st.write("#")
st.subheader("Analytical Skills")
st.write(
    """
- 💹 Data Analysis: I have expertise in data analysis across various platforms: R (leveraging tidyverse, tidymodels, modeltime, and more), Python (utilizing pandas, sklearn, sktime, among others), SPSS, and SQL.
- 📊 Dashboards and Data Visualization: Over recent years, I've acquired substantial hands-on experience with Microsoft PowerBi and have a foundational understanding of Tableau, inclusive of Tableau Prep.
-   Applications: Web applications showcasing analytical findings are frequently developed by me using Streamlit and Shiny. Within the Shiny framework, I primarily utilize the flexdashboard package.💻
    """
)
st.write("---")

# ---- Work history ----
st.subheader("Employment History")

# ---- Job 1 ----
st.write("🏢", "**Junior Consulting Data Scientist | Roland Berger**")
st.write("11/2023 - Present | Munich, Germany")
st.write(
    """
- Part of a team of tech and data-savvy strategy consultants
- Working as a client-facing data scientist (junior consultant)
- Industries: Healthcare, energy, and consumer goods
    """
)
st.write("#")

# ---- Job 2 ----
st.write("🏫", "**Research Associate People Analytics | Technical University of Applied Sciences Stuttgart**")
st.write("03/2023 - 10/2023 | Remote")
st.write(
    """
- Research project on predicting employee churn (data analysis using R)
- Leading the applied statistics tutorial (using R) for postgraduate students in Business Psychology (tree-based algorithms, regression, clustering, SEM)
    """
)
st.write("#")

# ---- Job 3 ----
st.write("📈", "**Strategy Consulting & Data Analytics | Roland Berger**")
st.write("10/2021 - 02/2023 | Munich, Germany / Edinburgh, UK / Bangkok, Thailand")
st.write(
    """
- A key pillar of the internal survey excellence team which manages large-scale market research initiatives in various industries (120,000+ participants)
- Development and deployment of a fully automated, cloud-native advanced analytics forecasting solution in the energy sector (using Python, R, SQL, AWS SageMaker & Power BI)
- Segmentation of customer profiles and derivation of strategic measures in the healthcare sector as part of a large-scale study; data preparation, data analysis, and data visualization with R
- Providing strategic advice to a global enterprise on the development and scaling of a blockchain-based marketplace for energy certificates
- Advising project teams & clients in various aspects of customer intelligence &  insights related topics (e.g., as part of a Due Diligence)
    """
)
st.write("#")

# ---- Job 4 ----
st.write("🚝", "**Customer Data & Market Analyst | Deutsche Bahn AG**")
st.write("08/2020 - 09/2021 | Frankfurt, Germany")
st.write(
    """
- Part of the customer analytics team, which acts as an in-house consulting unit for various topics related to customer data
- Creation of a weekly customer analytics report send out to 100+ employees, including the Chief Marketing Officer
- Conducting quantitative & qualitative market research (25+ studies/400,000+ participants) & analyzing large data sets using complex syntax (SPSS)
- Implementing measures to improve the quality of the company's travel information in order to significantly increase customer satisfaction
    """
)
st.write("---")

# ---- education ----
st.subheader("Education")

# ---- Education 1 ----
st.write("🎓", "**Master of Science - International Business Management | Edinburgh Napier University**")
st.write("09/2022 - 09/2023 | Edinburgh, UK")
st.write(
    """
- With distinction (85%+, best student in class of 200+)
- Majors: Strategy, innovation, leadership & marketing
- Topic of thesis: Understanding mental health in the consulting sector (marked 1.0 and will be published in an academic journal)
    """
)
st.write("#")

# ---- Education 2 ----
st.write("🎓", "**Master of Science - Business Psychology | Technical University of Applied Sciences Stuttgart**")
st.write("09/2021 - 09/2022 | Stuttgart, Germany")
st.write(
    """
- With distinction (1.2 with 1 = high & 5 = low, top 5 in class)
- Majors: Applied statistics, organizational psychology & consumer psychology
- Student representative business psychology
    """
)
st.write("#")

# ---- Education 3 ----
st.write("🎓", "**Bachelor of Science - Business Psychology | Darmstadt University of Applied Sciences**")
st.write("10/2017 - 09/2021 | Darmstadt, Germany")
st.write(
    """
- With distinction (1.2 with 1 = high & 5 = low, top 5 in class)
- Majors: Applied statistics, organizational psychology & consumer psychology
- Faculty council member social sciences & student representative business psychology
    """
)
st.write("#")

# ---- Education 4 ----
st.write("🎓", "**High School - A-levels | ARS Limburg**")
st.write("08/2013 - 06/2016 | Limburg, Germany")
st.write(
    """
- With distinction (1.3 with 1 = high & 6 = low; best student in class of 125)
- Majors: Mathematics & psychology
    """
)

# ---- widget section ----


def load_lottiefil(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


lottie_cv = load_lottiefil(
    "lottie/cv_lottie.json")

col3, col4, col5 = st.columns([1,2,1], gap="small")
with col3:
    st.write("")

with col4:
    st_lottie(
        lottie_cv,
        height=300,
        width=300
    )

with col5:
    st.write("")
