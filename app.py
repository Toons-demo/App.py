import streamlit as st
from datetime import datetime
st.write("Démarrage de Toons…")
import uuid

st.set_page_config(page_title="Toons – Commande IA", layout="centered")

st.title("📲 Interface Restaurateur – Toons")
st.subheader("Commandes reçues automatiquement par l'assistant vocal")

# Commandes simulées pour la démo
sample_orders = [
    {
        "id": str(uuid.uuid4())[:8],
        "heure": datetime.now().strftime("%H:%M"),
        "client": "Amine",
        "commande": "1 kebab galette, sauce blanche, sans oignons, avec frites et coca"
    },
    {
        "id": str(uuid.uuid4())[:8],
        "heure": datetime.now().strftime("%H:%M"),
        "client": "Lucia",
        "commande": "2 tacos, sauce samouraï et harissa, pain gratiné, coca zéro et oasis"
    },
    {
        "id": str(uuid.uuid4())[:8],
        "heure": datetime.now().strftime("%H:%M"),
        "client": "Youssef",
        "commande": "1 assiette kebab sans crudités, sauce algérienne, supplément fromage"
    },
]

# Affichage des commandes
for order in sample_orders:
    st.markdown(f"""
    ### 🧾 Commande #{order['id']}
    - 🕒 Heure : {order['heure']}
    - 👤 Client : {order['client']}
    - 🍽️ Détail : {order['commande']}
    ---
    """)

st.success("✅ Simulation active – les commandes s'afficheraient ici en temps réel.")


