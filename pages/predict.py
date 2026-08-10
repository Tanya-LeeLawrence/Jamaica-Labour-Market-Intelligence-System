import streamlit as st
import pandas as pd

#Load Model & Data
from utils.loader import (
    load_model,
    load_macro,
    load_feature_columns
)

from utils.mappings import *

model = load_model()
macro = load_macro()
feature_columns = load_feature_columns()


#Page Title
st.title(" Unemployment Risk Prediction")

st.markdown("""
Enter the individual's demographic information below.
The system combines the individual's characteristics with
national macroeconomic conditions for the selected year to
estimate the probability of unemployment.
""")

st.divider()

#User Input
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        100,
        25
    )

    sex_name = st.selectbox(
        "Sex",
        list(sex_mapping.keys())
    )

    parish_name = st.selectbox(
        "Parish",
        list(parish_mapping.keys())
    )

    area_name = st.selectbox(
        "Area of Residence",
        list(urcode_mapping.keys())
    )


with col2:

    relation_name = st.selectbox(
        "Relationship to Household Head",
        list(relationship_mapping.keys())
    )

    income_group = st.selectbox(
        "Income Category",
        [
            "Low",
            "Middle",
            "High"
        ]
    )

    year_options = sorted(
    macro["Year"].dropna().astype(int).unique()
)

    year = st.selectbox(
        "Survey Year",
        year_options
    )

st.divider()

# Predict Button
predict = st.button(
    "Predict",
    use_container_width=True,
    type="primary"
)

# Prediction Logic
if predict:

    sex = sex_mapping[sex_name]
    parish = parish_mapping[parish_name]
    urcode = urcode_mapping[area_name]
    relationship = relationship_mapping[relation_name]

    is_youth = int(age <= 24)
    is_prime = int(25 <= age <= 54)
    is_older = int(age >= 55)

    is_low_income = int(income_group == "Low")
    is_middle_income = int(income_group == "Middle")
    is_high_income = int(income_group == "High")

    macro_match = macro.loc[macro["Year"] == year]

    if macro_match.empty:
        st.error("Macroeconomic data not available for the selected year.")
        st.stop()

    macro_row = macro_match.iloc[0]

    input_df = pd.DataFrame({

        "AGE": [age],

        "SEX": [sex],

        "PAR": [parish],

        "URCODE": [urcode],

        "RELAT": [relationship],

        "YEAR": [year],

        "IS_YOUTH": [is_youth],

        "IS_PRIME": [is_prime],

        "IS_OLDER": [is_older],

        "IS_LOW_INCOME": [is_low_income],

        "IS_MIDDLE_INCOME": [is_middle_income],

        "IS_HIGH_INCOME": [is_high_income],

        "GDP_GROWTH": [macro_row["GDP_GROWTH"]],

        "Average_Annual_Sell_Rate": [
            macro_row["Average_Annual_Sell_Rate"]
        ],

        "Average_Annual_Interest_Rate": [
            macro_row["Average_Annual_Interest_Rate"]
        ],

        "Average_Annual_Inflation_Rate_AF": [
            macro_row["Average_Annual_Inflation_Rate_AF"]
        ],

        "IS_RECESSION": [
            macro_row["IS_RECESSION"]
        ],

        "IS_HIGH_INFLATION": [
            macro_row["IS_HIGH_INFLATION"]
        ],

        "IS_VERY_HIGH_INFLATION": [
            macro_row["IS_VERY_HIGH_INFLATION"]
        ],

        "IS_HIGH_INTEREST": [
            macro_row["IS_HIGH_INTEREST"]
        ],

        "IS_LOW_INTEREST": [
            macro_row["IS_LOW_INTEREST"]
        ],

        "IS_CURRENCY_DEPRECIATION": [
            macro_row["IS_CURRENCY_DEPRECIATION"]
        ],

        "IS_STRONG_DEPRECIATION": [
            macro_row["IS_STRONG_DEPRECIATION"]
        ]

    })

    # Match Training Feature Order
    input_df = input_df[feature_columns]
    input_df = input_df.astype(float)

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    # Prediction Result

    st.divider()

    st.header("Prediction Results")

    left, middle, right = st.columns(3)

    with left:

        if prediction == 1:

            st.error("Predicted Status")

            st.markdown("## Unemployed")

        else:

            st.success("Predicted Status")

            st.markdown("## Employed")

    with middle:

        st.metric(
            "Probability of Unemployment",
            f"{probability:.2%}"
        )

    with right:

        if probability < 0.30:

            risk = "Low"

        elif probability < 0.60:

            risk = "Moderate"

        else:

            risk = "High"

        st.metric(
            "Risk Level",
            risk
        )

    #probabilty visualization
    st.progress(
        float(probability),
        text=f"Estimated unemployment probability: "
             f"{probability:.1%}"
    )

    
    # Economic Conditions

    st.divider()

    st.subheader(
        f"Macroeconomic Environment — {year}"
    )


    
    # Get macro values
    

    # Calculate GDP growth for display
    current_year = int(macro_row["Year"])

    current_gdp = macro_row["GDP_GROWTH"]

    previous_gdp_rows = macro[
        macro["Year"].astype(int) == current_year - 1
    ]

    if (
        pd.notna(current_gdp)
        and not previous_gdp_rows.empty
        and pd.notna(previous_gdp_rows.iloc[0]["GDP_GROWTH"])
        and previous_gdp_rows.iloc[0]["GDP_GROWTH"] != 0
    ):

        previous_gdp = previous_gdp_rows.iloc[0]["GDP_GROWTH"]

        gdp_growth = (
            (float(current_gdp) - float(previous_gdp))
            / float(previous_gdp)
        ) * 100

    else:

        gdp_growth = None

    inflation = macro_row[
        "Average_Annual_Inflation_Rate_AF"
    ]

    interest_rate = macro_row[
        "Average_Annual_Interest_Rate"
    ]

    exchange_rate = macro_row[
        "Average_Annual_Sell_Rate"
    ]


    
    # GDP DISPLAY
    
    
    if pd.notna(gdp_growth):

        gdp_display = f"{float(gdp_growth):.2f}%"

    else:

        gdp_display = "N/A"


    
    # INFLATION DISPLAY
    

    if pd.notna(inflation):

        inflation_display = f"{float(inflation):.2f}%"

    else:

        inflation_display = "N/A"


   
    # INTEREST RATE DISPLAY
  

    if pd.notna(interest_rate):

        interest_display = f"{float(interest_rate):.2f}%"

    else:

        interest_display = "N/A"


    
    # EXCHANGE RATE DISPLAY
    

    if pd.notna(exchange_rate):

        exchange_display = f"{float(exchange_rate):.2f}"

    else:

        exchange_display = "N/A"


   
    # MACRO METRICS
   

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "GDP Growth",
            gdp_display
        )


    with col2:

        st.metric(
            "Inflation",
            inflation_display
        )


    with col3:

        st.metric(
            "Interest Rate",
            interest_display
        )


    with col4:

        st.metric(
            "Exchange Rate",
            exchange_display
        )


   
    # ECONOMIC FLAGS
    

    st.subheader("Economic Conditions")


    flag_col1, flag_col2, flag_col3 = st.columns(3)


    with flag_col1:

        if macro_row["IS_RECESSION"] == 1:

            st.error("🔴 Recession")

        else:

            st.success("🟢 No Recession")


    with flag_col2:

        if macro_row["IS_HIGH_INFLATION"] == 1:

            st.warning("🟠 High Inflation")

        elif macro_row["IS_VERY_HIGH_INFLATION"] == 1:

            st.error("🔴 Very High Inflation")

        else:

            st.success("🟢 Normal Inflation")


    with flag_col3:

        if macro_row["IS_HIGH_INTEREST"] == 1:

            st.warning("🟠 High Interest Rate")

        elif macro_row["IS_LOW_INTEREST"] == 1:

            st.info("🔵 Low Interest Rate")

        else:

            st.success("🟢 Normal Interest Rate")

    # Interpretation

    st.divider()

    st.subheader("Interpretation")

    if probability < 0.30:

        st.success("""
The model predicts that this individual has a relatively
low likelihood of unemployment under the selected
economic conditions.
""")

    elif probability < 0.60:

        st.warning("""
The prediction indicates a moderate unemployment risk.
Demographic characteristics together with macroeconomic
conditions suggest increased labour market vulnerability.
""")

    else:

        st.error("""
The model predicts a high probability of unemployment.
Individuals with similar characteristics experienced
higher unemployment rates during the selected economic
conditions.
""")

    # Suggested Actions

    st.divider()

    st.subheader("Suggested Actions")

    if probability < 0.30:

        st.info("""
• Continue workforce participation

• Maintain current skills

• Explore career development opportunities
""")

    elif probability < 0.60:

        st.info("""
• Participate in professional training

• Improve technical skills

• Expand employment search
""")

    else:

        st.info("""
• Prioritize employment support programmes

• Register with labour market services

• Consider skills development initiatives

• Seek career counselling opportunities
""")

    st.divider()

    st.caption("""
Prediction generated using the XGBoost model developed for
the COMP6830 Capstone Project.
""")