import pandas as pd
import statsmodels.formula.api as smf


def analyser_regression_multiple(df):
    if df is None:
        print(" ARRÊT : Les données sont manquantes pour la régression multiple.")
        return

    # régression linéaire multiple
    print(" RÉGRESSION LINÉAIRE MULTIPLE ")


    # Equation  régression multiple :
    # Note = β0 + (β1 * clics) + (β2 * jours) + (β3 * composants) + (β4 * contextes) + (β5 * temps)+ (β6 * nombre de test)
    formule = "note ~ nb_clics + nb_jours + nb_composants + nb_contextes + temps_total_sec+ nb_tests"

    # Calcul des meilleurs coefficients β pour minimiser l'erreur
    modele = smf.ols(formula=formule, data=df).fit()

    # Affichage du résumé statistique
    print(modele.summary())

    # Explication des formules
    print("FORMULES UTILISÉES")
    print(f"1. Modèle : Y = Xβ + ε (où Y est la note et X les indicateurs)")
    print(f"2. R-squared (R²) : {modele.rsquared:.2f}")
    print(f" Cela signifie que {modele.rsquared * 100:.0f}% de la note est expliquée par l'activité ARCHE.")

    # Interprétation de la p_value (F-statistic)
    p_value = modele.f_pvalue
    print(f"3. Prob (F-statistic) : {p_value:.4e}")

    if p_value < 0.05:
        print(f"Comme la p-value ({p_value:.4e}) est inférieure à 0.05,")
        print(" le modèle global est statistiquement significatif.")
    else:
        print(f"Comme la p-value ({p_value:.4e}) est supérieure à 0.05,")
        print("le modèle n'est pas considéré comme statistiquement significatif.")


# Bloc de test
if __name__ == "__main__":
    from load import charger_donnees
    from cleaner import nettoyage_donnees
    from features import calculer_indicateurs


    # 1. Préparation des données (Chargement -> Nettoyage -> Indicateurs)
    df_logs, df_notes = charger_donnees()
    df_logs_clean, df_notes_clean = nettoyage_donnees(df_logs, df_notes)
    df_final = calculer_indicateurs(df_logs_clean, df_notes_clean)

    # 2. Lancement de la régression multiple
    analyser_regression_multiple(df_final)