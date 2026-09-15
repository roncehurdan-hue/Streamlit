import streamlit as st


def afficher_filtres(df):
    st.sidebar.header("Filtres d'analyse")

    leagues = ["Toutes"] + sorted(df["League"].dropna().unique().tolist())
    selected_league = st.sidebar.selectbox("Sélectionner une Ligue :", leagues)

    positions = ["Tous"] + sorted(df["Position"].dropna().unique().tolist())
    selected_position = st.sidebar.selectbox("Sélectionner un Poste :", positions)

    genders = ["Tous", "Masculin (M)", "Féminin (F)"]
    gender_raw = st.sidebar.selectbox("Sélectionner le Genre :", genders)

    if gender_raw == "Masculin (M)":
        selected_gender = "M"
    elif gender_raw == "Féminin (F)":
        selected_gender = "F"
    else:
        selected_gender = "Tous"

    selected_ovr = st.sidebar.slider(
        "Seuil OVR :",
        int(df["OVR"].min()),
        int(df["OVR"].max()),
        (int(df["OVR"].min()), int(df["OVR"].max())),
    )

    selected_dri = st.sidebar.slider(
        "Dribble minimum DRI :",
        int(df["DRI"].min()),
        int(df["DRI"].max()),
        int(df["DRI"].min()),
    )

    selected_pac = st.sidebar.slider(
        "Vitesse minimum PAC :",
        int(df["PAC"].min()),
        int(df["PAC"].max()),
        int(df["PAC"].min()),
    )

    return (
        selected_league,
        selected_position,
        selected_gender,
        selected_ovr,
        selected_dri,
        selected_pac,
    )
