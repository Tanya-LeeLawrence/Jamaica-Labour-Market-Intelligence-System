import pandas as pd
import pickle
import numpy as np
import xgboost as xgb
import streamlit as st

MODEL_PATH = "models/"
DATA_PATH = "data/"


class XGBModel:
    def __init__(self, booster):
        self._booster = booster

    def predict(self, df):
        dmatrix = xgb.DMatrix(df)
        proba = self._booster.predict(dmatrix)
        return (proba > 0.5).astype(int)

    def predict_proba(self, df):
        dmatrix = xgb.DMatrix(df)
        proba = self._booster.predict(dmatrix)
        return np.column_stack([1 - proba, proba])


@st.cache_resource
def load_model():

    booster = xgb.Booster()
    booster.load_model(
        f"{MODEL_PATH}xgboost_unemployment_model.json"
    )

    return XGBModel(booster)


@st.cache_resource
def load_feature_columns():

    with open(
        f"{MODEL_PATH}feature_columns.pkl",
        "rb"
    ) as f:

        features = pickle.load(f)

    return features


@st.cache_data
def load_macro():

    return pd.read_csv(
        f"{DATA_PATH}Final_Macroeconomic.csv"
    )