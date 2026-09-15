import streamlit as st


def afficher_meilleurs_profils(selection):
    """Affiche les 20 meilleurs joueurs selon les critères."""

    st.subheader("Meilleurs profils disponibles")

    st.write(
        "Les joueurs sont classés par note générale, "
        "puis par vitesse et par dribble."
    )

    colonnes = [
        "Name",
        "Age",
        "Nation",
        "Team",
        "League",
        "Position",
        "OVR",
        "PAC",
        "DRI",
        "SHO",
        "PAS",
        "PHY"
    ]

    classement = (
        selection[colonnes]
        .sort_values(
            by=["OVR", "PAC", "DRI"],
            ascending=[False, False, False]
        )
        .head(20)
    )

    st.dataframe(
        classement,
        use_container_width=True,
        hide_index=True
    )