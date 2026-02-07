import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="FAO Analytics - Dashboard", layout="wide")

@st.cache_data
def load_and_preprocess():
    # Chargement (Assurez-vous que les fichiers sont dans le même dossier)
    pop = pd.read_csv('population.csv')
    sn = pd.read_csv('sous_nutrition.csv')
    aide = pd.read_csv('aide_alimentaire.csv')
    dispo = pd.read_csv('dispo_alimentaire.csv')
    
    # Nettoyage Population
    pop['population'] = pop['Valeur'] * 1000
    
    # Nettoyage Sous-nutrition
    sn['annee_clean'] = sn['Année'].str.extract('(\d{4})').astype(int) + 1
    sn['nb_sn'] = pd.to_numeric(sn['Valeur'].replace('<0.1', 0.05), errors='coerce').fillna(0) * 1_000_000
    
    # Jointure pour les taux annuels (df_sn)
    df_sn = pd.merge(
        sn[['Zone', 'annee_clean', 'nb_sn']], 
        pop[['Zone', 'Année', 'population']], 
        left_on=['Zone', 'annee_clean'], 
        right_on=['Zone', 'Année']
    )
    df_sn['taux_sn'] = (df_sn['nb_sn'] / df_sn['population']) * 100
    
    return df_sn, aide, dispo

# Chargement des données
df_sn, df_aide, df_dispo = load_and_preprocess()

# --- BARRE LATÉRALE ---
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Aller vers :", 
    ["Situation & Évolution", "Aide Alimentaire", "Focus Exportations (Taux > 7%)"])

# --- PAGE 1 : SITUATION & ÉVOLUTION ---
if page == "Situation & Évolution":
    st.title("🌍 Situation Mondiale")
    data_2017 = df_sn[df_sn['annee_clean'] == 2017]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Population (2017)", f"{data_2017['population'].sum()/1e9:.2f} Md")
    col2.metric("Sous-nutrition (2017)", f"{data_2017['nb_sn'].sum()/1e6:.1f} M")
    col3.metric("Proportion", f"{(data_2017['nb_sn'].sum()/data_2017['population'].sum())*100:.2f} %")
    
    st.divider()
    st.subheader("📈 Évolution temporelle")
    evol_m = df_sn.groupby('annee_clean').agg({'nb_sn':'sum', 'population':'sum'}).reset_index()
    evol_m['taux'] = (evol_m['nb_sn'] / evol_m['population']) * 100
    st.plotly_chart(px.line(evol_m, x='annee_clean', y='taux', markers=True, title="Tendance Mondiale (%)"))

# --- PAGE 2 : AIDE ALIMENTAIRE ---
elif page == "Aide Alimentaire":
    st.title("🤝 Analyse des Aides")
    top_benef = df_aide.groupby('Pays bénéficiaire')['Valeur'].sum().sort_values(ascending=False).head(10).reset_index()
    st.plotly_chart(px.bar(top_benef, x='Valeur', y='Pays bénéficiaire', orientation='h', title="Top 10 Bénéficiaires"))

# --- PAGE 3 : FOCUS EXPORTATIONS ---
elif page == "Focus Exportations (Taux > 7%)":
    st.title("🚢 Paradoxe des Exportations")
    
    # Identification des pays > 7% en 2017
    data_2017 = df_sn[df_sn['annee_clean'] == 2017]
    pays_cibles_df = data_2017[data_2017['taux_sn'] > 7].copy()
    pays_cibles_liste = sorted(pays_cibles_df['Zone'].unique())
    
    st.info(f"Il y a **{len(pays_cibles_liste)}** pays avec un taux > 7% de sous-nutrition.")

    # Sélecteur
    pays_sel = st.selectbox("Sélectionnez un pays :", pays_cibles_liste)
    
    # Infos pays
    info_pays = pays_cibles_df[pays_cibles_df['Zone'] == pays_sel].iloc[0]
    st.metric(f"Taux de sous-nutrition ({pays_sel})", f"{info_pays['taux_sn']:.2f} %")

    # Calcul des exports
    detail = df_dispo[df_dispo['Zone'] == pays_sel].copy()
    detail = detail[detail['Exportations - Quantité'] > 0] # On garde les exports réels
    
    # Calcul du ratio
    detail['% exporté/production'] = (detail['Exportations - Quantité'] / detail['Production']) * 100
    detail.replace([float('inf')], 100, inplace=True) # Gestion des stocks (export > production)

    st.subheader(f"Top 10 des produits exportés par {pays_sel}")
    top_10 = detail.sort_values('Exportations - Quantité', ascending=False).head(10)
    
    # Affichage stylisé
    st.dataframe(top_10[[
        'Produit', 'Exportations - Quantité', 'Production', '% exporté/production', 'Disponibilité intérieure'
    ]].style.format({'% exporté/production': '{:.1f}%'}))