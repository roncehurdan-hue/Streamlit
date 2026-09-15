import streamlit as st

from constantes.playerelo_api import rechercher_joueurs, recuperer_valeur


def _nom_joueur(joueur):
    return str(joueur.get("player_name") or joueur.get("name") or "Joueur inconnu")


def _id_joueur(joueur):
    return joueur.get("player_id") or joueur.get("id")


def _extraire_valeur(payload):
    if not isinstance(payload, dict):
        return payload

    data = payload.get("data") if isinstance(payload.get("data"), dict) else payload
    for cle in ("market_value_eur", "market_value", "value_eur", "value"):
        if cle in data and data[cle] is not None:
            return data[cle]
    return None


def afficher_recherche_playerelo():
    st.subheader("Recherche PlayerElo")
    st.write(
        "Recherchez un joueur par son nom pour obtenir son identifiant "
        "PlayerElo et sa valeur marchande calculée."
    )

    nom = st.text_input(
        "Nom du joueur",
        placeholder="Exemple : Haaland",
        key="recherche_playerelo",
    )

    if not nom:
        return

    try:
        joueurs = rechercher_joueurs(nom)
    except Exception as erreur:
        st.error(f"La recherche PlayerElo a échoué : {erreur}")
        return

    if not joueurs:
        st.warning("Aucun joueur PlayerElo trouvé pour ce nom.")
        return

    choix = st.selectbox(
        "Joueur trouvé",
        options=range(len(joueurs)),
        format_func=lambda index: _nom_joueur(joueurs[index]),
    )

    joueur = joueurs[choix]
    player_id = _id_joueur(joueur)

    if not player_id:
        st.warning("PlayerElo n'a pas renvoyé d'identifiant pour ce joueur.")
        return

    st.write(f"Identifiant PlayerElo : {player_id}")

    try:
        payload_valeur = recuperer_valeur(player_id)
        st.json(payload_valeur)
        valeur = _extraire_valeur(payload_valeur)
    except Exception as erreur:
        st.error(f"Impossible de récupérer la valeur marchande : {erreur}")
        return

    if valeur is None:
        st.warning("La valeur marchande n'est pas disponible pour ce joueur.")
    elif isinstance(valeur, (int, float)):
        st.metric("Valeur marchande estimée", f"{valeur:,.0f} €".replace(",", " "))
    else:
        st.metric("Valeur marchande estimée", str(valeur))
