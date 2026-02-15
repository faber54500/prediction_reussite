import pandas as pd
from cleaner import nettoyage_donnees
from load import charger_donnees

def calculer_indicateurs(df_logs_clean, df_notes_clean):
    if df_logs_clean is None or df_notes_clean is None:
        print("\n[!] ERREUR (features.py) : Les données nettoyées sont absentes (None).")
        print("    -> Le calcul des indicateurs ne peut pas être effectué.")
        return None

    print("Création du tableau avec les indicateurs de suivi")

    # ---------------------------------------------------------
    # 1. VOLUME : Nombre total de clics
    # ---------------------------------------------------------
    # Création d'une colonne de comptage de clic par étudiant
    comptage_vol = df_logs_clean['pseudo'].value_counts()
    df_volume = pd.DataFrame({'pseudo': comptage_vol.index,'nb_clics': comptage_vol.values})

    # ---------------------------------------------------------
    # 2. RÉGULARITÉ : Nombre de jours différents de connexion
    # ---------------------------------------------------------
    # Création d'une colonne  du nombre de jours différents de connexion par étudiant
    df_logs_clean['jour'] = df_logs_clean['heure'].dt.date
    comptage_reg = df_logs_clean.groupby('pseudo')['jour'].nunique()
    df_regularite = pd.DataFrame({'pseudo': comptage_reg.index,'nb_jours': comptage_reg.values})

    # ---------------------------------------------------------
    # 3. DIVERSITÉ : Nombre d'outils différents (Test, Fichier...)
    # ---------------------------------------------------------
    # Création d'une colonne  du nombre d'outils différents utilisé par étudiant
    comptage_div = df_logs_clean.groupby('pseudo')['composant'].nunique()
    df_diversite = pd.DataFrame({'pseudo': comptage_div.index,'nb_composants': comptage_div.values})

    # ---------------------------------------------------------
    # 4. ÉTENDUE : Nombre de ressources/chapitres consultés
    # ---------------------------------------------------------
    # Création du nombre de ressources/chapitres consultés par étudiant
    comptage_ete = df_logs_clean.groupby('pseudo')['contexte'].nunique()
    df_etendue = pd.DataFrame({'pseudo': comptage_ete.index,'nb_contextes': comptage_ete.values})

    # ---------------------------------------------------------
    # 5. TEMPS : Somme des sessions (Règle des 300 secondes)
    # ---------------------------------------------------------
    #  les actions par élève sont rangées par ordre chronologique
    df_logs_clean = df_logs_clean.sort_values(by=['pseudo', 'heure'])

    # calcule du temps écoulé (en secondes) entre deux clics consécutifs
    df_logs_clean['ecart'] = df_logs_clean.groupby('pseudo')['heure'].diff().dt.total_seconds()

    #  les écarts < 300s sont gardés (on ignore les pauses de plus de 300 s (5 min))
    petits_ecarts = df_logs_clean[df_logs_clean['ecart'] < 300]

    # On additionne les petits écarts pour chaque élève
    somme_tps = petits_ecarts.groupby('pseudo')['ecart'].sum()

    # Création du tableau de synthèse
    df_temps = pd.DataFrame({'pseudo': somme_tps.index,'temps_total_sec': somme_tps.values})

    #----------------------------------------------------------
    # 6. PERFORMANCE : Nombre d'évaluations (tests)
    # ---------------------------------------------------------
    #  les lignes où l'activité est un 'test' sont captées
    df_logs_tests = df_logs_clean[df_logs_clean['composant'] == 'Test']

    # Comptage des lignes par étudiant
    comptage_tests = df_logs_tests['pseudo'].value_counts()

    df_tests = pd.DataFrame({'pseudo': comptage_tests.index, 'nb_tests': comptage_tests.values})

    # ---------------------------------------------------------
    # 7. FUSION FINALE (injection des zéros)
    # ---------------------------------------------------------
    # On part du tableau des NOTES (les 99 étudiants officiels)
    df_final = df_notes_clean.copy()

    # On fusionne chaque petit tableau un par un avec aussi les 4 qui n'ont pas de clics
    df_final = pd.merge(df_final, df_volume, on='pseudo', how='left')
    df_final = pd.merge(df_final, df_regularite, on='pseudo', how='left')
    df_final = pd.merge(df_final, df_diversite, on='pseudo', how='left')
    df_final = pd.merge(df_final, df_etendue, on='pseudo', how='left')
    df_final = pd.merge(df_final, df_temps, on='pseudo', how='left')
    df_final = pd.merge(df_final, df_tests, on='pseudo', how='left')

    # remplacement de  tous les vides (NaN) par 0 pour ceux qui ne se sont pas connectés à ARCHE
    df_final = df_final.fillna(0)

    print(f"l'étude va porter sur {len(df_final)} étudiants ")

    #  Vérifications finales
    print("VÉRIFICATION DU TABLEAU FINAL")
    print(f"Nombre total de lignes : {len(df_final)} ")
    print("\nAperçu des 5 premières lignes :")
    print(df_final.head())

    # Verification de ceux qui ne se sont pas connectés sur ARCHE sont bien présent  filtre sur nb_clics == 0
    print("\nÉtudiants qui n'ont jamais ouvert ARCHE (Vérification injection) :")
    print(df_final[df_final['nb_clics'] == 0])


    print(f"l'étude va porter sur {len(df_final)} étudiants ")
    return df_final


if __name__ == "__main__":
    # Chargement des données brutes
    df_logs_brut, df_notes_brut = charger_donnees()

    # nettoyage des données
    df_logs_clean, df_notes_clean = nettoyage_donnees(df_logs_brut, df_notes_brut)

    # calcule des indicateurs
    resultat = calculer_indicateurs(df_logs_clean, df_notes_clean)



