import streamlit as st


def afficher_indicateurs(selection):
    """Affiche les chiffres clés des joueurs sélectionnés."""

    colonne1, colonne2, colonne3, colonne4 = st.columns(4)

    colonne1.metric(
        "Joueurs trouvés",
        len(selection)
    )

    colonne2.metric(
        "OVR moyen",
        round(selection["OVR"].mean(), 1)
    )

    colonne3.metric(
        "PAC moyen",
        round(selection["PAC"].mean(), 1)
    )

    colonne4.metric(
        "DRI moyen",
        round(selection["DRI"].mean(), 1)
    )