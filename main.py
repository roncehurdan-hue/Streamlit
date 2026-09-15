import streamlit as st

from constantes.input_data import charger_donnees
from sources.barre_filtre import afficher_filtres
from sources.analyse.analyse import afficher_indicateurs
from sources.analyse.filtre import filtrer_donnees, afficher_meilleurs_profils
from sources.analyse.playerelo_vue import afficher_recherche_playerelo
from sources.graphique.line import afficher_histogramme, afficher_barplot
from sources.graphique.scatter import afficher_scatter


st.set_page_config(
    page_title="Cellule de recrutement",
    page_icon="⚽",
    layout="wide",
)


def main():
    st.title("⚽ Tableau de bord de recrutement")
    st.write(
        "Cet outil permet de rechercher des joueurs selon leur championnat, "
        "leur poste, leur genre et leurs performances."
    )

    with st.expander("Rechercher la valeur marchande d'un joueur avec PlayerElo"):
        afficher_recherche_playerelo()

    df = charger_donnees()

    (
        selected_league,
        selected_position,
        selected_gender,
        selected_ovr,
        selected_dri,
        selected_pac,
    ) = afficher_filtres(df)

    selection = filtrer_donnees(
        df,
        selected_league,
        selected_position,
        selected_gender,
        selected_ovr,
        selected_dri,
        selected_pac,
    )

    if selection.empty:
        st.warning(
            "Aucun joueur ne correspond aux critères. "
            "Diminuez les seuils ou modifiez les filtres."
        )
        st.stop()

    afficher_indicateurs(selection)
    st.divider()

    afficher_histogramme(selection)
    st.divider()

    afficher_barplot(selection)
    st.divider()

    afficher_scatter(selection)
    st.divider()

    afficher_meilleurs_profils(selection)


if __name__ == "__main__":
    main()
