import streamlit as st
import os

print("Current working directory:", os.getcwd())
print("Config file exists:", os.path.exists(".streamlit/config.toml"))

st.set_page_config(
    page_title="Portfolio de Claire Mercier",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1519751138087-5bf79df62d5b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
        }
        [data-testid="stSidebar"] {
        background-color: transparent; /* Couleur de fond */
        background-size: cover;
        min-width: 250px; /* Largeur minimale */
        max-width: 250px; /* Largeur maximale */
        }
        html, body, [class*="css"], h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #2e2e36 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Création du menu
with st.sidebar:
    st.markdown(
        """
        <h2 style="font-weight: bold; margin-bottom: -40px; margin-top: 30px">Menu</h2>
        """,
        unsafe_allow_html=True
    )
    selection = st.radio(
        "",
        ("Qui suis-je ?", "Dashboard \"Indices de Développement Humain\"", "Dashboard de KPI Toys & Models", "Moteur de recommandation de films")
    )

def afficher_contenu(selection):
    if selection == "Qui suis-je ?":
        st.markdown(
        """
        <h3 style="font-weight: bold;">Bienvenue sur mon portfolio !</h2>
        <p>Bonjour ! 👋</p>
        <p>Moi c'est Claire Mercier. 😁</p>
        Initialement ingénieur agro 🍕 et docteur en microbiologie 🔬 de formation, j'ai décidé en 2024 de suivre une formation de Data Analyst avec la 
        <a href="https://www.wildcodeschool.com/fr-fr/formation-data-analyst" target="_blank" style="text-decoration: bold;"> 
        Wild Code School </a>.</p>
        <p>Je suis passionnée depuis toujours par les sciences, les données et la programmation. J'aime apprendre constamment et relever de 
        nouveaux défis 💪 et la data me semble le terrain de jeu idéal pour cela !</p>
        <p>Ce portfolio, en cours de réalisation, vous permettra de voir les différents projets que j'ai pu réaliser grâce
        à mes nouvelles compétences :</p>
        <ul>
            <li><b>🐍 Langages de programmation :</b> Python, SQL, HTML/CSS, PHP.</li>
            <li><b>🐼 Analyse de données et machine learning : </b>Pandas, Numpy, Scikit-learn, web scraping.</li>
            <li><b>📊 Visualisation de données : </b>Power BI, Matplotlib, Seaborn, Plotly Express.</li>
            <li><b>🦆 Gestion de bases de données et cloud: </b>MySQL, DuckDB, AWS, MageAI, DBT.</li>
        </ul>
        <p>Pour plus d'informations sur mon parcours, vous pouvez consulter <a href="https://github.com/SeaJayEm/portfolio/blob/f6ef243ea4e8a14aa7178b1ec3025937693292cd/images/CV%20Claire%20Mercier%202025%20FR.pdf" target="_blank" style="text-decoration: bold;">
        mon CV</a> ou encore passer me dire bonjour sur <a href="https://www.linkedin.com/in/clairemercier/" target="_blank" style="text-decoration: bold;">linkedin</a> !</p>
        <p><i>À très bientôt et, en attendant, je vous souhaite une bonne visite !</i></p>
        """,
        unsafe_allow_html=True
    )
  
    elif selection == "Dashboard \"Indices de Développement Humain\"":
        st.markdown(
        """
        <h2 style="font-weight: bold;">Projet de Dashboard sur les indices de développement humain</h2>
        """,
        unsafe_allow_html=True
        )
        st.markdown(
            '''
            <p>Ce dashboard a été créé à partir de <a href="https://www.kaggle.com/datasets/iamsouravbanerjee/human-development-index-dataset" target="_blank" style="text-decoration: bold;">données</a> de la Banque Mondiale et de l'ONU. 
            Il permet de visualiser les indices de développement humain (IDH) des différents pays du monde entier 🌎.</p>
            <p>Le premier onglet permet d'observer l'évolution de l'IDH de 1990 à 2021 📈 et montre bien l'impact de Covid ou de la guerre sur celui-ci. 
            Le deuxième onglet se focalise sur l'année 2021 📷, la dernière année disponible dans le dataset utilisé, tandis que le troisième onglet 
            permet d'afficher l'IDH, l'IDH ajusté aux inégalités, l'IDH ajusté à la durabilité, 
            et l'indice d'égalité entre les genres par pays et par année. N'hésitez-pas à faire vos propres recherches sur cet outil 💡 !</p>
            <iframe title="HDI" width="740" height="473.5" src="https://app.powerbi.com/view?r=eyJrIjoiZjUyZWZjNjUtNzY4NC00ZjJjLWEzYzctY2Y3NmY1MTM4MWYxIiwidCI6IjkzZGMyZjFmLWM1MTUtNGMzYi04ZDlhLTY5YjM3NjcwZGJlZSJ9" frameborder="0" allowFullScreen="true"></iframe>'
            <br><br>
            <p>Voici la stack technique utilisée pour ce mini projet :</p>
            <ul>
                <li>Nettoyage et préparation des données avec Python 🐍 / Pandas 🐼</li>
                <li>Visualisation de données avec Power BI 📊</li>
            </ul>
            <p>Un des challenges liés à ce projet a été de nettoyer les données et de les préparer pour la visualisation. En effet, le jeu de données initial
            comportait pas moins de 880 colonnes. J'ai donc commencé par transformer ce jeu de données grâce à Pandas afin de passer
            d'un dataframe de 880 colonnes à un dataframe avec 40 colonnes dont une indiquant l'année: </p>
            ''',
            unsafe_allow_html=True)
        st.image("https://github.com/SeaJayEm/portfolio/raw/refs/heads/main/images/df_before")
        st.image("https://github.com/SeaJayEm/portfolio/raw/refs/heads/main/images/df_after")

    elif selection == "Dashboard de KPI Toys & Models":
        st.markdown(
        """
        <h2 style="font-weight: bold;">Projet de Dashboard de KPI pour l'entreprise Toys & Models</h2>
        <p>Ce projet a été réalisé avec mon équipe de la Wilde Code School. L'objectif était la conception d’un tableau de bord interactif pour Toys & Models, 
        une entreprise spécialisée dans les maquettes et jouets réduits 🚗.</p>
        <p>Les KPI demandés par le client portaient sur :</p>
        <ul>
            <li>Les résultats commerciaux (onglet 1)</li>
            <li>La performance financière (onglet 2)</li>
            <li>Les aspects logistiques (onglet 3)</li>
            <li>Les indicateurs RH (onglet 4)</li>
        </ul>
        <iframe title="dashboard_toys_and_models (1)" width="740" height="473.5" src="https://app.powerbi.com/view?r=eyJrIjoiMTIzOWJkMzYtNmJlNS00ZjZhLTljMjctZjE5MmRhMTA1NWFlIiwidCI6IjkzZGMyZjFmLWM1MTUtNGMzYi04ZDlhLTY5YjM3NjcwZGJlZSJ9" frameborder="0" allowFullScreen="true"></iframe>
        <p>Voici la stack technique utilisée pour ce projet :</p>
            <ul>
                <li>Analyse des données via le schéma de base de données fourni 🔎</li>
                <li>Rédaction de requêtes SQL afin de relier différentes tables et obtenir des informations pertinentes sur la performance de l'entreprise 💡</li>
                <li>Visualisation de données avec Power BI 📊</li>
                <li>Travail en mode Agile 🏃</li>
            </ul>

        """,
        unsafe_allow_html=True
        )

    elif selection == "Moteur de recommandation de films":
        st.markdown(
        """
        <h2 style="font-weight: bold;">Projet de moteur de recommandation de films</h2>
        <p>Ce projet a été réalisé avec mon équipe de la Wilde Code School. L'objectif était de créer un moteur de 
        recommandation de films 🎥 pour un cinéma (fictif) de la Réunion.</p>
        <p>Notre étude de marché préalable a été basée sur l'extraction des données d'un site réunionnais spécialisé dans
        le cinéma 🍿 par webscraping. Notre analyse a démontré que les réunionnais avaient une préférence pour le cinéma des années 60 à 70.
        Nous avons donc décidé de proposer à notre client un outil lui permettant de rechercher des films et des courts métrages similaires afin d'organiser des festivals ou soirées à thème.</p> 
        <p>Le résultat ?</p>
        <p>Une application intuitive qui recommande des films en quelques secondes, idéale pour inspirer des programmations créatives !</p>
        <p>Je vous invite à la tester <a href="https://codebusters-wcs.streamlit.app/" target="_blank" style="text-decoration: bold;">ici
        </a> afin de (re)-découvrir le cinéma des années 60 et 70.</p> 
        <p>Voici la stack technique utilisée pour ce projet :</p>
            <ul>
                <li>🦆 DuckDB pour récupérer les données filtrées des BDD IMDB et TMDB</li>
                <li>🐼 Pandas et Numpy pour le nettoyage et la transformation du dataset de 1100 films</li>
                <li>📊 Visualisation des données avec Matplotlib et Seaborn</li>
                <li>💬 NLP avec NLTK (WordNetLemmatizer, stopwords)</li>
                <li>🤖 Machine Learning avec Scikit-learn (CountVectorizer, cosine_similarity)</li>
                <li>💻 Création d'une application avec Streamlit</li>
            </ul>
 
        """,
        unsafe_allow_html=True
        )



# Affichage du contenu en fonction de la sélection
afficher_contenu(selection)

