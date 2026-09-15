import requests
import streamlit as st


BASE_URL = "https://data-api.playerelo.football"


def _headers():
    api_key = st.secrets.get("PLAYER_ELO_API_KEY", "")
    if not api_key:
        raise ValueError("La clé PLAYER_ELO_API_KEY est absente des secrets Streamlit.")
    return {"Authorization": f"Bearer {api_key}"}


@st.cache_data(ttl=3600, show_spinner=False)
def rechercher_joueurs(nom):
    """Recherche des joueurs PlayerElo à partir de leur nom."""
    nom = nom.strip()
    if len(nom) < 2:
        return []

    response = requests.get(
        f"{BASE_URL}/v1/players",
        headers=_headers(),
        params={"search": nom, "limit": 20},
        timeout=15,
    )
    response.raise_for_status()
    payload = response.json()

    if isinstance(payload, list):
        joueurs = payload
    elif isinstance(payload, dict):
        joueurs = (
            payload.get("players")
            or payload.get("data")
            or payload.get("results")
            or []
        )
    else:
        joueurs = []

    nom_minuscule = nom.casefold()
    return [
        joueur
        for joueur in joueurs
        if nom_minuscule
        in str(joueur.get("player_name") or joueur.get("name") or "").casefold()
    ]


@st.cache_data(ttl=3600, show_spinner=False)
def recuperer_valeur(player_id):
    """Récupère la valeur marchande calculée d'un joueur."""
    response = requests.get(
        f"{BASE_URL}/v1/players/{player_id}/value",
        headers=_headers(),
        timeout=15,
    )
    response.raise_for_status()
    return response.json()
