import streamlit as st
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURATION FIXE (Modifie ici tes vraies infos) ---
INFOS = {
    "nom": "TON NOM / ENTREPRISE",
    "siret": "123 456 789 00012",
    "adresse": "10 Rue de l'Exemple, 75000 Paris",
    "client": "NOM DU CLIENT FIXE",
    "tarif": 12.50
}

st.set_page_config(page_title="Pointage Express", page_icon="📝")

st.header("📝 Ma Facture de Journée")
st.write("Remplissez l'heure de fin et téléchargez le PDF.")

# Entrées simples
col1, col2 = st.columns(2)
with col1:
    date_j = st.date_input("Date", datetime.now())
    n_fac = st.text_input("N° Facture", datetime.now().strftime("%Y%m%d"))
with col2:
    h_fin = st.number_input("Heure de fin (ex: 18.5 pour 18h30)", min_value=10.0, max_value=23.9, value=18.0, step=0.25)

# Calculs
duree = h_fin - 10.0
total = duree * INFOS["tarif"]

if st.button("Générer le PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"FACTURE N° {n_fac}", ln=1)
    
    pdf.set_font("Arial", size=10)
    pdf.ln(5)
    pdf.cell(0, 5, f"{INFOS['nom']} - SIRET: {INFOS['siret']}", ln=1)
    pdf.cell(0, 5, INFOS['adresse'], ln=1)
    pdf.ln(10)
    pdf.cell(0, 5, f"Facturé à : {INFOS['client']}", ln=1)
    pdf.ln(10)
    
    # Détail
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(100, 10, "Description", 1)
    pdf.cell(40, 10, "Heures", 1)
    pdf.cell(40, 10, "Total HT", 1, ln=1)
    
    pdf.set_font("Arial", size=11)
    pdf.cell(100, 10, f"Travail du {date_j.strftime('%d/%m/%Y')}", 1)
    pdf.cell(40, 10, f"{duree}h", 1)
    pdf.cell(40, 10, f"{total:.2f} €", 1, ln=1)
    
    # Téléchargement
    html_pdf = pdf.output(dest='S')
    st.download_button("⬇️ Cliquez ici pour télécharger", data=bytes(html_pdf), file_name=f"Facture_{n_fac}.pdf")
    st.success("Facture prête !")
