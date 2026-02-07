# 🌍 Dashboard FAO : Étude de Santé Publique sur la Sous-Nutrition

Ce projet consiste en une application interactive développée avec **Streamlit** pour analyser les données de l'Organisation des Nations Unies pour l'alimentation et l'agriculture (FAO). L'objectif est d'explorer les indicateurs de sécurité alimentaire, l'efficacité des aides internationales et les paradoxes commerciaux des pays en situation de stress alimentaire.

## 🚀 Aperçu de l'Application

Le dashboard est divisé en trois sections principales :
1.  **Situation Mondiale & Évolution** : Visualisation des indicateurs clés (KPIs) de 2017 et des tendances de sous-nutrition de 2013 à 2018.
2.  **Aide Alimentaire** : Analyse des pays bénéficiaires et des types de produits envoyés en aide.
3.  **Paradoxe des Exportations** : Focus sur les pays ayant un taux de sous-nutrition > 7% et analyse de leurs exportations agricoles.



## 🛠️ Installation et Lancement Local

Suivez ces étapes pour faire fonctionner l'application sur votre machine :

### 1. Cloner le dépôt
```bash
git clone [https://github.com/votre-username/votre-depot-fao.git](https://github.com/votre-username/votre-depot-fao.git)
cd votre-depot-fao

Voici un fichier README.md complet, professionnel et prêt à l'emploi pour votre dépôt GitHub. Il est structuré pour expliquer clairement le projet à un recruteur ou à un collaborateur.

Markdown
# 🌍 Dashboard FAO : Étude de Santé Publique sur la Sous-Nutrition

Ce projet consiste en une application interactive développée avec **Streamlit** pour analyser les données de l'Organisation des Nations Unies pour l'alimentation et l'agriculture (FAO). L'objectif est d'explorer les indicateurs de sécurité alimentaire, l'efficacité des aides internationales et les paradoxes commerciaux des pays en situation de stress alimentaire.

## 🚀 Aperçu de l'Application

Le dashboard est divisé en trois sections principales :
1.  **Situation Mondiale & Évolution** : Visualisation des indicateurs clés (KPIs) de 2017 et des tendances de sous-nutrition de 2013 à 2018.
2.  **Aide Alimentaire** : Analyse des pays bénéficiaires et des types de produits envoyés en aide.
3.  **Paradoxe des Exportations** : Focus sur les pays ayant un taux de sous-nutrition > 7% et analyse de leurs exportations agricoles.



## 🛠️ Installation et Lancement Local

Suivez ces étapes pour faire fonctionner l'application sur votre machine :

### 1. Cloner le dépôt
```bash
git clone [https://github.com/votre-username/votre-depot-fao.git](https://github.com/votre-username/votre-depot-fao.git)
cd votre-depot-fao
2. Installer les dépendances
Il est recommandé d'utiliser un environnement virtuel.

Bash
pip install -r requirements.txt
3. Lancer l'application
Bash
streamlit run santApp.py
📊 Données utilisées
L'analyse repose sur quatre fichiers de données (FAOSTAT) :

population.csv : Historique de la population par pays.

sous_nutrition.csv : Nombre de personnes en sous-nutrition par périodes de 3 ans.

aide_alimentaire.csv : Historique des livraisons d'aide par pays et produit.

dispo_alimentaire.csv : Bilans alimentaires (Production, Exportation, Disponibilité).

🧮 Méthodologie
Nettoyage : Conversion des unités (milliers vers unités réelles), traitement des valeurs seuils (ex: <0.1 remplacé par 0.05 pour les calculs).

Temporalité : Alignement des périodes triennales de la FAO sur des années centrales numériques pour permettre une analyse chronologique.

Indicateurs : Calcul du taux de sous-nutrition (Population malnutrie / Population totale) et du ratio d'exportation (Export / Production).

📦 Structure du projet
Plaintext
├── santApp.py            # Code source de l'application Streamlit
├── requirements.txt      # Liste des bibliothèques Python nécessaires
├── population.csv        # Données sources
├── sous_nutrition.csv    # Données sources
├── aide_alimentaire.csv  # Données sources
├── dispo_alimentaire.csv # Données sources
└── README.md             # Documentation
✒️ Auteur
Jemaiz - Data Scientist
