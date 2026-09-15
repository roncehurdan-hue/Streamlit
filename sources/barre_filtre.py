import streamlit as st


CINQ_GRANDS_CHAMPIONNATS = [
    "Premier League",
    "LALIGA EA SPORTS",
    "Bundesliga",
    "Serie A Enilive",
    "Ligue 1 McDonald's"
]


def appliquer_filtres(df):
    st.sidebar.header("Filtres de recrutement")

    hors_top_5 = st.sidebar.checkbox(
        "Hors des cinq grands championnats",
        value=True
    )

    liste_ligues = sorted(df["League"].dropna().unique())
    liste_postes = sorted(df["Position"].dropna().unique())

    postes_par_defaut = [
        poste for poste in ["LW", "RW", "LM", "RM"]
        if poste in liste_postes
    ]

    ligues = st.sidebar.multiselect(
        "Championnat",
        options=liste_ligues
    )

    postes = st.sidebar.multiselect(
        "Poste",
        options=liste_postes,
        default=postes_par_defaut
    )

    ovr_min = st.sidebar.slider(
        "Note générale minimale OVR",
        min_value=int(df["OVR"].min()),
        max_value=int(df["OVR"].max()),
        value=75
    )

    pac_min = st.sidebar.slider(
        "Vitesse minimale PAC",
        min_value=int(df["PAC"].min()),
        max_value=int(df["PAC"].max()),
        value=80
    )

    dri_min = st.sidebar.slider(
        "Dribble minimal DRI",
        min_value=int(df["DRI"].min()),
        max_value=int(df["DRI"].max()),
        value=75
    )

    selection = df[
        (df["OVR"] >= ovr_min)
        & (df["PAC"] >= pac_min)
        & (df["DRI"] >= dri_min)
    ].copy()

    if hors_top_5:
        selection = selection[
            ~selection["League"].isin(CINQ_GRANDS_CHAMPIONNATS)
        ]

    if ligues:
        selection = selection[
            selection["League"].isin(ligues)
        ]

    if postes:
        selection = selection[
            selection["Position"].isin(postes)
        ]

    return selection