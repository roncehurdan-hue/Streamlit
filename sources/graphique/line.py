import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def afficher_histogramme(selection):
    """Affiche la distribution des notes OVR."""

    st.subheader("Distribution des notes générales")

    st.write(
        "Cet histogramme montre comment les notes générales "
        "des joueurs sélectionnés sont réparties."
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.histplot(
        data=selection,
        x="OVR",
        bins=10,
        kde=True,
        color="#2A78D6",
        ax=ax
    )

    ax.set_title("Répartition des joueurs selon leur note générale")
    ax.set_xlabel("Note générale OVR")
    ax.set_ylabel("Nombre de joueurs")
    ax.set_xlim(40, 99)

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


def afficher_barplot(selection):
    """Compare la moyenne OVR des championnats."""

    st.subheader("Comparaison des championnats")

    st.write(
        "Ce graphique compare la note générale moyenne "
        "des joueurs dans les différents championnats."
    )

    moyennes = (
        selection.groupby("League", as_index=False)
        .agg(
            OVR_moyen=("OVR", "mean"),
            Nombre_joueurs=("Name", "count")
        )
        .sort_values("OVR_moyen", ascending=False)
        .head(6)
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.barplot(
        data=moyennes,
        x="OVR_moyen",
        y="League",
        hue="League",
        palette="Blues_r",
        legend=False,
        ax=ax
    )

    # Les barres commencent à zéro
    ax.set_xlim(0, 100)

    ax.set_title("Les championnats aux meilleures moyennes OVR")
    ax.set_xlabel("Note générale moyenne OVR")
    ax.set_ylabel("Championnat")

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)