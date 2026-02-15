import pandas as pd

# récupération des fichiers provenant de load
def nettoyage_donnees (df_logs, df_notes) :
    # si le chargement a échoué un message d'erreur apparait
    if df_logs is None or df_notes is None :
        print ("il n'est pas possible de nettoyer les données car il y a un souci pour la lecture des fichiers logs.csv et notes.csv")
        return None, None
    try :
        # on vérifie si il n'y a pas de duplica dans notes.csv
        nb_avant = len(df_notes)
        df_notes_clean = df_notes.drop_duplicates()
        if (nb_avant - len(df_notes_clean)) == 0:
            print(f"le nombre de doublon dans notes.csv est de {nb_avant - len(df_notes_clean)} ")
            print("il n'y a donc pas de doublon")
        elif (nb_avant - len(df_notes_clean)) > 0:
            print(f"le nombre de doublon dans notes.csv est de {nb_avant - len(df_notes_clean)} ")
            # Vérification finale des doublons
            nb_doublons_final = df_notes_clean.duplicated().sum()
            print(f"VÉRIFICATION : Nombre de doublons restants dans notes : {nb_doublons_final}")
            print("les doublons ont été supprimés")

        # conversion des dates avec coerse si une case n'est pas convertie correctement  une case vide sera mise en place
        df_logs['heure'] = pd.to_datetime(df_logs['heure'], errors='coerce')
        nb_erreurs_date = df_logs['heure'].isna().sum()
        if nb_erreurs_date == 0:
            print("Toutes les dates ont été converties correctement")
        elif nb_erreurs_date > 0:
            print(f"le nombre de date non converties est de {nb_erreurs_date} ")
            # subset cible uniquement la case heure pour les suppressions
            df_logs = df_logs.dropna(subset=['heure'])
            # Vérification finale des dates
            nb_erreurs_date_final = df_logs['heure'].isna().sum()
            print(f"VÉRIFICATION : Nombre de dates non converties (NaT) restantes : {nb_erreurs_date_final}")
            print(f"les {nb_erreurs_date} dates non converties ont été supprimées ")


        # comparaison des etudiants dans logs et notes
        nb_etudiants_notes = df_notes_clean['pseudo'].nunique()
        nb_etudiants_logs_avant = df_logs['pseudo'].nunique()

        print("Comparaison avant nettoyage")
        print(f"Étudiants dans le fichier NOTES : {nb_etudiants_notes}")
        print(f"Étudiants dans le fichier LOGS  : {nb_etudiants_logs_avant}")

        # On regarde les étudiants présent dans logs (étudiant unique)
        etudiants_avec_notes = df_notes_clean['pseudo'].unique()

        # On ne garde que les clics des étudiants qui sont dans le fichier notes
        df_logs_clean = df_logs[df_logs['pseudo'].isin(etudiants_avec_notes)]

        # Comparaison apres nettoyage
        nb_logs_final = df_logs_clean['pseudo'].nunique()

        print("Comparaison après nettoyage")
        print(f"Étudiants dans le fichier NOTES : {nb_etudiants_notes}")
        print(f"Étudiants dans le fichier LOGS  : {nb_logs_final}")
        return df_logs_clean, df_notes_clean

    except Exception as erreur_inconnue:
        print(f" ERREUR IMPRÉVUE lors du nettoyage des données : {erreur_inconnue}")
        return None, None

if __name__ == "__main__":
    import pandas as pd

    # valeur incorrecte pour test logs et notes
    data_logstest = {
        'pseudo': ['436', '841', '436','18'],
        'heure': ['2024-07-24 09:48:08', '2024-07-24 09:48:08', 'HEURE', '2024-08-24 09:48:08'],  #  date invalide
        'contexte': ['Cours', 'Cours', 'Cours','Cours']
    }

    data_notestest = {'pseudo': ['436','436', '841'], 'note': [12, 12, 15]}

    # conversion en dataframe
    df_logs_test = pd.DataFrame(data_logstest)
    df_notes_test = pd.DataFrame(data_notestest )

    # test unitaire
    nettoyage_donnees(df_logs_test, df_notes_test)
