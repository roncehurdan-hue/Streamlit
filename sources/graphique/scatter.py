import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def afficher_scatter(selection):
    """Affiche la relation entre vitesse et dribble."""

    st.subheader("Relation entre vitesse et dribble")

    st.write(
        "Les joueurs placés en haut à droite sont les profils "
        "les plus rapides et les meilleurs dribbleurs."
    )

    donnees = selection.copy()

    # Conserver cinq championnats et regrouper les autres
    top_5_ligues = (
        donnees["League"]
        .value_counts()
        .head(5)
        .index
    )

    donnees["Groupe_ligue"] = donnees["League"].where(
        donnees["League"].isin(top_5_ligues),
        "Autres"
    )

    fig, ax = plt.subplots(figsize=(9, 6))

    sns.scatterplot(
        data=donnees,
        x="PAC",
        y="DRI",
        hue="Groupe_ligue",
        size="OVR",
        sizes=(40, 180),
        alpha=0.7,
        palette="Set2",
        ax=ax
    )

    ax.set_xlim(20, 99)
    ax.set_ylim(20, 99)

    ax.set_title(
        "Les meilleurs profils combinent vitesse et dribble"
    )

    ax.set_xlabel("Vitesse PAC")
    ax.set_ylabel("Dribble DRI")

    ax.legend(
        title="Championnat et OVR",
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)