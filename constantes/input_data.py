from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def charger_donnees():
    chemin_csv = (
        Path(__file__).resolve().parents[1]
        / "all_players_clean.csv"
    )

    df = pd.read_csv(chemin_csv)

    df = df.dropna(
        subset=[
            "Name",
            "League",
            "Position",
            "OVR",
            "PAC",
            "DRI"
        ]
    )

    return df