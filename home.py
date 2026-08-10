import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Jamaica Labour Market Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# HEADER
# ============================================================

st.title("Jamaica Labour Market Intelligence System")

st.markdown(
    """
    ### Data driven insights into unemployment and labour market vulnerability

    The **Jamaica Labour Market Intelligence System** is a machine
    learning decision support application developed to examine
    unemployment risk among individuals in Jamaica.

    The system combines **individual demographic and socioeconomic
    characteristics** from the Jamaica Labour Force Survey with
    **national macroeconomic conditions** to estimate the likelihood
    of unemployment for a selected year.

    The project was developed as part of the **COMP6830 Capstone Project**
    and is motivated by the need to better understand the factors
    associated with unemployment, including the perception that
    individuals may become less employable as they grow older.
    """
)


# ============================================================
# QUICK NAVIGATION
# ============================================================

st.divider()

st.subheader("Explore the System")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Unemployment Prediction")

    st.write(
        """
        Enter an individual's characteristics and select
        a survey year to estimate their unemployment risk.
        """
    )

    st.page_link(
        "pages/predict.py",
        label="**Make a Prediction**",

    )
    


with col2:
    st.markdown("### About the System")

    st.write(
        """
        Learn about the project, data sources, methodology,
        model and intended application of the system.
        """
    )

    st.page_link(
        "pages/about.py",
        label="**About the Project**",
        
    )
    

# ============================================================
# HOW THE SYSTEM WORKS
# ============================================================

st.divider()

st.header("How the System Works")

steps = [
    (
        "1️⃣",
        "Individual Information",
        "The user enters demographic and socioeconomic characteristics."
    ),
    (
        "2️⃣",
        "Economic Context",
        "The system retrieves the macroeconomic conditions associated with the selected year."
    ),
    (
        "3️⃣",
        "Feature Preparation",
        "The information is transformed into the format required by the trained machine learning model."
    ),
    (
        "4️⃣",
        "Prediction",
        "The XGBoost model estimates the probability of unemployment."
    ),
    (
        "5️⃣",
        "Decision Support",
        "The system presents the prediction, risk level and relevant economic context."
    )
]

for icon, title, description in steps:

    col1, col2 = st.columns([1, 8])

    with col1:
        st.markdown(f"## {icon}")

    with col2:

        st.markdown(f"**{title}**")

        st.write(description)



# ============================================================
# IMPORTANT INTERPRETATION
# ============================================================

st.divider()

st.header("Important Note")

st.info(
    """
    **This system is a decision support tool, not a hiring or
    employment decision system.**

    A predicted unemployment probability should not be interpreted
    as a definitive statement about an individual's employability.
    The model identifies patterns learned from historical data and
    should be considered alongside professional judgement,
    labour market information and other relevant evidence.
    """
)    


