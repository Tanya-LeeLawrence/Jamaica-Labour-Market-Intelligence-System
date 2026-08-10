import streamlit as st




#Page Title
st.title("About")

# ============================================================
# PROJECT PURPOSE
# ============================================================

st.divider()

st.header("Why This System Was Developed")

st.markdown(
    """
    Employment outcomes are influenced by a combination of
    individual characteristics and broader economic conditions.

    One of the motivations for this project is the perception that
    **older individuals may become less employable as they age**.
    Rather than relying on assumptions alone, this project uses
    historical labour market data to investigate whether demographic
    characteristics and economic conditions are associated with
    differences in unemployment risk.

    The system therefore provides an analytical approach for
    examining labour market vulnerability and identifying patterns
    that may be useful to researchers, policymakers and employment
    support organisations.
    """
)


# ============================================================
# DATA SOURCES
# ============================================================

st.divider()

st.header("Data Sources")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Jamaica Labour Force Survey")

    st.write(
        """
        Labour market and demographic information from the
        **Statistical Institute of Jamaica (STATIN)** was used
        to represent individual characteristics associated with
        employment outcomes.
        """
    )


with col2:

    st.subheader("Macroeconomic Indicators")

    st.write(
        """
        Macroeconomic indicators from the **Bank of Jamaica (BOJ)**
        were incorporated to represent the wider economic environment
        in which individuals participate in the labour market.
        """
    )

# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.header("Best Model Performance")

st.markdown(
    """
    Several experimental configurations were evaluated to determine
    whether adding macroeconomic and newspaper derived information
    improved unemployment prediction beyond the core JLFS variables.
    """
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Best Model",
        "XGBoost"
    )

with col2:

    st.metric(
        "Accuracy",
        "76.49%"
    )

with col3:

    st.metric(
        "F1-Score",
        "71.61%"
    )

with col4:

    st.metric(
        "ROC-AUC",
        "0.8372"
    )


st.caption(
    "Best performing configuration: JLFS + Macroeconomic Indicators."
)



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


# ============================================================
# PROJECT VALUE
# ============================================================

st.divider()

st.header("Potential Value")

col1, col2 = st.columns(2)

with col1:

    st.subheader("For Labour Market Planning")

    st.markdown(
        """
        - Identify patterns associated with unemployment
        - Examine differences across demographic groups
        - Consider the influence of economic conditions
        - Support evidence based labour market analysis
        """
    )


with col2:
    

    st.subheader("For Employment Support")

    st.markdown(
        """
        - Identify groups that may require additional support
        - Inform skills development initiatives
        - Support targeted employment programmes
        - Provide additional evidence for resource planning
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    """
    Jamaica Labour Market Intelligence System |
    COMP6830 Capstone Project
    """
)

st.caption(
    "Developed as an academic prototype for labour market analysis "
    "and machine learning decision support."
)