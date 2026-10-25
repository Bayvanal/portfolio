

PROJECTS = [

    # ==========================================

    # PROJET 1 : MERGEAI

    # ==========================================

    {

        "slug": "mergeai",

        "title": "MergeAI",

        "category": "Développement · Intelligence artificielle",



        "summary": (

            "Application web de résolution de conflits Git "

            "assistée par intelligence artificielle."

        ),

        "architecture_description": (
            "Du conflit Git fourni par l'utilisateur "
            "jusqu'à la proposition de résolution assistée par IA."
        ),

        "architecture_label": "MERGEAI / AZURE OPENAI",





        "description": (
            "MergeAI est une application web développée avec Django "
            "pour analyser des conflits Git et proposer une résolution "
            "avec Azure OpenAI. Elle identifie les versions HEAD et incoming, "
            "propose un code fusionné et explique les modifications. "
            "Chaque résolution doit être vérifiée avant utilisation."
        ),

        "technologies": [

            "Python",

            "Django",

            "Azure OpenAI",

            "Docker",

            "Git",

        ],



        "features": [

            "Saisie d'un conflit Git dans une interface web.",

            "Sélection du langage de programmation.",

            "Identification des versions HEAD et incoming.",

            "Analyse du conflit avec Azure OpenAI.",

            "Génération d'une proposition de code fusionné.",

            "Explication de la résolution proposée.",

        ],



        "image": "images/projects/mergeai.png",



        "website": "https://mergeai.bayvan.fyi",

        "github": None,



        "video_id": "gCbOfTYj8LE",



        "architecture": [

            {

                "icon": "monitor",

                "title": "Interface utilisateur",

                "description": (

                    "Saisie du conflit Git et sélection "

                    "du langage de programmation."

                ),

            },

            {

                "icon": "server",

                "title": "Backend Django",

                "description": (

                    "Réception de la requête et "

                    "orchestration du traitement."

                ),

            },

            {

                "icon": "git-merge",

                "title": "Git Parser",

                "description": (

                    "Extraction des versions HEAD "

                    "et incoming du conflit."

                ),

            },

            {

                "icon": "brain-circuit",

                "title": "Azure OpenAI",

                "description": (

                    "Analyse du conflit et génération "

                    "d'une proposition de résolution."

                ),

            },

            {

                "icon": "check-circle-2",

                "title": "Résultat",

                "description": (

                    "Présentation du code fusionné "

                    "et de son explication."

                ),

            },

        ],



        "technical_choices": [

            {

                "title": "Django",

                "description": (

                    "Framework Python utilisé pour "

                    "structurer le backend et gérer "

                    "les interactions avec l'interface."

                ),

            },

            {

                "title": "Azure OpenAI",

                "description": (

                    "Service d'intelligence artificielle "

                    "utilisé pour analyser les conflits "

                    "et proposer une résolution."

                ),

            },

            {

                "title": "Docker",

                "description": (

                    "Conteneurisation de l'application "

                    "pour simplifier son déploiement."

                ),

            },

        ],



        "gallery": [

            {

                "image": "images/projects/mergeai-resolution.png",

                "caption": (

                    "Exemple de résolution d'un conflit Git."

                ),

            },

        ],

    },



    # ==========================================

    # PROJET 2 : DATA JOBS

    # ==========================================



    {

        "slug": "data-jobs",

        "title": "Data Jobs",

        "category": "Data Science · Machine Learning",



        "summary": (

            "Application interactive de classification des métiers "

            "Data à partir des compétences techniques."

        ),



        "description": (
            "Data Jobs est une application Python et Streamlit qui explore "
            "les liens entre les compétences techniques et les métiers "
            "Data Analyst, Data Engineer et Data Scientist. Un modèle de "
            "classification entraîné sur des offres d'emploi françaises "
            "classe les métiers selon les compétences sélectionnées. "
            "L'application présente également les compétences les plus "
            "fréquentes dans les annonces de chaque métier."
        ),


        "architecture_description": (
            "Du traitement des offres d'emploi à la classification "
            "des métiers Data selon les compétences sélectionnées."
        ),

        "architecture_label": "DATA JOBS / MACHINE LEARNING",

        "technologies": [

            "Python",

            "Streamlit",

            "Pandas",

            "scikit-learn",

            "Joblib",

        ],



        "features": [

            (

                "Sélection interactive des compétences "

                "à partir du vocabulaire du modèle."

            ),

            (

                "Classement des métiers Data selon "

                "les scores du modèle de classification."

            ),

            (

                "Visualisation des résultats sous forme "

                "de tableau et de graphique."

            ),

            (

                "Exploration des compétences fréquentes "

                "pour Data Analyst, Data Engineer et Data Scientist."

            ),

            (

                "Identification des compétences fréquentes "

                "absentes de la sélection actuelle."

            ),

            (

                "Déduplication des annonces pour limiter "

                "le poids des republications dans les statistiques."

            ),

        ],



        "image": "images/projects/data-jobs.png",



        "website": "https://datajobs.bayvan.fyi",

        "github": None,

        "video_id": None,



        "architecture": [

            {

                "icon": "database",

                "title": "Corpus d'offres d'emploi",

                "description": (

                    "Chargement du jeu de données préparé "

                    "contenant les métiers et compétences "

                    "issus des offres françaises."

                ),

            },

            {

                "icon": "filter",

                "title": "Analyse des compétences",

                "description": (

                    "Déduplication des groupes d'annonces, "

                    "extraction des compétences et calcul "

                    "de leurs fréquences par métier."

                ),

            },

            {

                "icon": "brain-circuit",

                "title": "Modèle de classification",

                "description": (

                    "Chargement d'un modèle sauvegardé avec "

                    "Joblib et classement des métiers "

                    "selon les compétences sélectionnées."

                ),

            },

            {

                "icon": "monitor",

                "title": "Interface Streamlit",

                "description": (

                    "Sélection des compétences, affichage "

                    "des scores et exploration des "

                    "compétences fréquentes par métier."

                ),

            },

        ],



        "technical_choices": [
            {
                "title": "Random Forest",
                "description": (
                    "Modèle de classification supervisée avec pondération "
                    "des classes, évalué sur un jeu de test indépendant."
                ),
            },
            {
                "title": "CountVectorizer",
                "description": (
                    "Transformation des compétences en variables binaires "
                    "indiquant leur présence ou leur absence."
                ),
            },
            {
                "title": "Streamlit et Pandas",
                "description": (
                    "Interface interactive, classement des métiers et "
                    "calcul des fréquences de compétences par métier."
                ),
            },
        ],

        "model_metrics": [
            {"value": "98,3 %", "label": "Accuracy sur le test"},
            {"value": "98,4 %", "label": "F1 macro sur le test"},
            {"value": "59", "label": "Compétences représentées"},
        ],

        "gallery": [],

    },





    # ==========================================

    # PROJET 3 : PIPELINE ETL

    # ==========================================

    
    {
        "slug": "pipeline-etl",
        "title": "Pipeline ETL",
        "category": "Data Engineering · Intégration de données",

        "summary": (
            "Pipeline ETL développé avec Talend pour intégrer, "
            "nettoyer et enrichir des données multi-sources."
        ),

        "description": (
            "Ce projet consiste à construire un pipeline ETL "
            "avec Talend afin d'intégrer des données issues "
            "de fichiers CSV, d'une base MySQL et d'une API REST. "
            "Les traitements comprennent le contrôle de la "
            "qualité des données, l'harmonisation des formats, "
            "les jointures, les agrégations et l'enrichissement "
            "par des taux de change. "
            "L'objectif est de produire des données cohérentes "
            "et exploitables pour des analyses ultérieures."
        ),

        "technologies": [
            "Talend",
            "SQL",
            "MySQL",
            "Java",
            "API REST",
            "ETL",
        ],

        "features": [
            (
                "Extraction et intégration de données "
                "depuis des fichiers CSV et MySQL."
            ),
            (
                "Contrôle des formats de dates et "
                "validation des données."
            ),
            (
                "Nettoyage, filtrage et déduplication "
                "des enregistrements."
            ),
            (
                "Jointures et transformations avec tMap."
            ),
            (
                "Agrégation des données avec Talend."
            ),
            (
                "Récupération de taux de change "
                "depuis une API REST."
            ),
            (
                "Enrichissement des données "
                "et export des résultats."
            ),
        ],

        "image": "images/projects/talend.png",

        "website": None,
        "github": None,
        "video_id": None,

        "architecture_description": (
            "Des sources de données hétérogènes "
            "jusqu'à leur transformation et leur "
            "enrichissement dans un pipeline ETL."
        ),

        "architecture_label": "TALEND / ETL PIPELINE",

        "architecture": [
            {
                "icon": "database",
                "title": "Sources de données",
                "description": (
                    "Chargement des données issues "
                    "de fichiers CSV, de MySQL "
                    "et d'une API REST."
                ),
            },
            {
                "icon": "filter",
                "title": "Nettoyage et validation",
                "description": (
                    "Vérification des formats, "
                    "contrôle des dates, filtrage "
                    "et gestion des doublons."
                ),
            },
            {
                "icon": "git-merge",
                "title": "Transformation et enrichissement",
                "description": (
                    "Jointures, agrégations et "
                    "intégration des taux de change "
                    "à l'aide des composants Talend."
                ),
            },
            {
                "icon": "file-output",
                "title": "Export des données",
                "description": (
                    "Production de jeux de données "
                    "nettoyés et transformés."
                ),
            },
        ],

        "technical_choices": [
            {
                "title": "Talend",
                "description": (
                    "Conception visuelle des flux ETL "
                    "avec des composants dédiés "
                    "à l'extraction et aux transformations."
                ),
            },
            {
                "title": "SQL et MySQL",
                "description": (
                    "Exploitation de données relationnelles "
                    "et intégration avec les flux Talend."
                ),
            },
            {
                "title": "API REST",
                "description": (
                    "Récupération de taux de change "
                    "pour enrichir les données "
                    "avec des informations externes."
                ),
            },
        ],


        "gallery": [
            {
                "image": "images/projects/talend.png",
                "caption": (
                    "Vue d'ensemble du pipeline ETL et "
                    "des différents flux de traitement."
                ),
            },
            {
                "image": "images/projects/talend-transformations.png",
                "caption": (
                    "Détail des jointures, des transformations "
                    "et des agrégations intermédiaires."
                ),
            },
            {
                "image": "images/projects/talend-sorties.png",
                "caption": (
                    "Dernières étapes de traitement, "
                    "répartition des flux et sorties du pipeline."
                ),
            },
        ],

    },


]
