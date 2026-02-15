import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from features import calculer_indicateurs

def analyser_regressions(df):
    if df is None:
        print(" ARRÊT : Les données sont manquantes. Vérifiez vos fichiers logs.csv ou notes.csv.")
        return

    print("\n--- ANALYSE PAR RÉGRESSION LINÉAIRE ---")

    #  indicateurs à tester
    indicateurs = ['nb_clics', 'nb_jours', 'nb_composants', 'nb_contextes', 'temps_total_sec','nb_tests' ]

    for col in indicateurs:
        # identification des données
        x = df[col]
        y = df['note']

        # Calcul de la régression
        res = stats.linregress(x, y)

        # Affichage des résultats
        print(f"\nIndicateur : {col}")
        print(f"  Coefficient de corrélation (r) : {res.rvalue:.2f}")
        print(f"  Coefficient de détermination (r²) : {res.rvalue ** 2:.2f}")
        print(f"  Équation : Note = {res.slope:.2f} * {col} + {res.intercept:.2f}")


if __name__ == "__main__":
    from load import charger_donnees
    from cleaner import nettoyage_donnees

    # 1. Préparation des données (Chargement -> Nettoyage -> Indicateurs)
    df_logs, df_notes = charger_donnees()
    df_logs_clean, df_notes_clean = nettoyage_donnees(df_logs, df_notes)
    df_final = calculer_indicateurs(df_logs_clean, df_notes_clean)

    # 2. Lancement de la régression
    analyser_regressions(df_final)

