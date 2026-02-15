import pandas as pd
import matplotlib.pyplot as plt

def exploration_data(df_logs_clean, df_notes_clean):

    # Nombre d'élèves différents
    nb_eleves = df_logs_clean['pseudo'].nunique()
    print(f"Nombre d'étudiants actifs dans les logs : {nb_eleves}")

    # Nombre de cours différents
    nb_cours = df_logs_clean['contexte'].nunique()
    print(f"Nombre de ressources (cours/chapitres) consultées : {nb_cours}")

    # Top 5 des activités les plus fréquentes
    print("Top 5 des types d'actions :")
    print(df_logs_clean['evenement'].value_counts().head(5).to_string(name=False, dtype=False))


def voir_les_absents(df_logs_clean, df_notes_clean):
    print("Visaulisation des étudiant sans activité sur ARCHE")

    # liste des étudiant qui ont eu au moins une activité
    liste_actifs = list(df_logs_clean['pseudo'].unique())

    # création liste vide de ceux qui n'ont pas utilisé ARCHE
    pseudos_absents = []

    # Pour chaque étudiant présent dans le fichier des notes
    for pseudo_etudiant in df_notes_clean['pseudo'].unique():
        # si l'étudiant n'apparaît pas dans la liste des actifs
        if pseudo_etudiant not in liste_actifs:
            # Alors ajout aux absents
            pseudos_absents.append(pseudo_etudiant)

    # Affichage de ceux qui ne se sont pas connecté sur ARCHE avec leur note respective
    df_resultat = df_notes_clean[df_notes_clean['pseudo'].isin(pseudos_absents)]

    print(f"Voici les {len(df_resultat)} étudiants qui n'ont jamais ouvert ARCHE :")
    print(df_resultat[['pseudo', 'note']])

    print(" 5 premières lignes du tableau de logs nettoyé :")
    print(df_logs_clean.head(5))

    return pseudos_absents


if __name__ == "__main__":
    from load import charger_donnees
    from cleaner import nettoyage_donnees

    # récupération des données brutes (df_logs, df_notes)
    df_logs, df_notes = charger_donnees()

    if df_logs is not None:
        # récupération  des données nettoyées (df_logs_clean, df_notes_clean)
        df_logs_clean, df_notes_clean = nettoyage_donnees(df_logs, df_notes)

        # exploration avec les données nettoyées
        exploration_data(df_logs_clean, df_notes_clean)

        # affichage des étudiants qui n'ont pas été sur arche et de leur note
        absents = voir_les_absents(df_logs_clean, df_notes_clean)
