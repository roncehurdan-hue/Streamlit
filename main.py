import streamlit as st

from constantes.input_data import charger_donnees
from sources.barre_filtre import appliquer_filtres
from sources.analyse.analyse import afficher_indicateurs
from sources.analyse.filtre import afficher_meilleurs_profils
from sources.graphique.line import (
    afficher_histogramme,
    afficher_barplot
)
from sources.graphique.scatter import afficher_scatter


st.set_page_config(
    page_title="Cellule de recrutement",
    page_icon="⚽",
    layout="wide"
)


def main():
    st.title("⚽ Tableau de bord de recrutement")

    st.write(
        "Cet outil permet de trouver des ailiers rapides et bons "
        "dribbleurs, avec une note générale supérieure à 75 et "
        "évoluant hors des cinq grands championnats."
    )

    # Charger les joueurs
    df = charger_donnees()

    # Appliquer les filtres
    selection = appliquer_filtres(df)

    # Gérer une sélection vide
    if selection.empty:
        st.warning(
            "Aucun joueur ne correspond aux critères. "
            "Diminuez les seuils ou modifiez les filtres."
        )
        st.stop()

    # Bandeau des chiffres clés
    afficher_indicateurs(selection)

    st.divider()

    # Distribution
    afficher_histogramme(selection)

    st.divider()

    # Comparaison entre les championnats
    afficher_barplot(selection)

    st.divider()

    # Relation entre vitesse et dribble
    afficher_scatter(selection)

    st.divider()

    # Tableau des meilleurs profils
    afficher_meilleurs_profils(selection)


if __name__ == "__main__":
    main()